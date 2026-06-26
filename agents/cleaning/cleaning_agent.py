"""
cleaning_agent.py

Version : 1.0.0

Cleaning Agent

Responsibilities
----------------
1. Read validated datasets
2. Clean datasets
3. Save cleaned datasets
4. Save cleaning metadata
5. Generate reports
"""

from datetime import datetime
from pathlib import Path

from agents.base.base_agent import (
    BaseAgent,
    AgentResult,
    AgentStatus
)

from readers.reader_factory import ReaderFactory
from writers.writer_factory import WriterFactory

from agents.cleaning.cleaning_rules import CleaningRules
from agents.cleaning.cleaning_report import CleaningReport

from database.repositories.dataset_repository import DatasetRepository
from database.repositories.cleaning_repository import CleaningRepository

from config.cleaning_config import (
    CLEANED_DATASET_DIRECTORY,
    EXPORT_FORMAT
)


class CleaningAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.dataset_repository = DatasetRepository()

        self.cleaning_repository = CleaningRepository()

    # ==========================================================
    # Clean Single Dataset
    # ==========================================================

    def clean_dataset(
        self,
        file_path: str
    ):

        file_path = Path(file_path)

        # ------------------------------------------------------
        # Read Dataset
        # ------------------------------------------------------

        reader = ReaderFactory.get_reader(file_path)

        reader_result = reader.read()

        dataframe = reader_result.dataframe

        # ------------------------------------------------------
        # Clean Dataset
        # ------------------------------------------------------

        cleaning_result, cleaned_dataframe = (

            CleaningRules.clean_dataset(

                dataframe,

                dataset_name=file_path.stem

            )

        )

        # ------------------------------------------------------
        # Output Path
        # ------------------------------------------------------

        output_path = (

            CLEANED_DATASET_DIRECTORY /

            f"{file_path.stem}.{EXPORT_FORMAT}"

        )

        # ------------------------------------------------------
        # Save Clean Dataset
        # ------------------------------------------------------

        writer = WriterFactory.get_writer(

            output_path

        )

        writer.write(

            cleaned_dataframe,

            output_path

        )

        # ------------------------------------------------------
        # Reports
        # ------------------------------------------------------

        report = CleaningReport()

        txt_report = report.save_txt(

            cleaning_result

        )

        report.save_json(

            cleaning_result

        )

        # ------------------------------------------------------
        # Save Cleaning Metadata
        # ------------------------------------------------------

        self.cleaning_repository.save_result(

            file_path=str(file_path),

            cleaning_time=cleaning_result.cleaning_time,

            cleaning_status=cleaning_result.status.value,

            rows_before=cleaning_result.summary.rows_before,

            rows_after=cleaning_result.summary.rows_after,

            duplicates_removed=cleaning_result.summary.duplicates_removed,

            null_rows_removed=cleaning_result.summary.null_rows_removed,

            null_columns_removed=cleaning_result.summary.null_columns_removed,

            columns_standardized=cleaning_result.summary.columns_standardized,

            data_types_converted=cleaning_result.summary.data_types_converted,

            output_path=str(output_path)

        )

        # ------------------------------------------------------
        # Update Dataset Status
        # ------------------------------------------------------

        self.dataset_repository.mark_cleaned(

            str(file_path)

        )

        return cleaning_result
    
    # ==========================================================
    # Execute
    # ==========================================================

    def execute(self):

        datasets = self.dataset_repository.get_validated_datasets()

        processed = 0
        failed = 0
        skipped = 0

        errors = []

        for row in datasets:

            file_path = row[0]

            try:

                self.clean_dataset(file_path)

                processed += 1

                print(
                    f"✅ Cleaned : {Path(file_path).name}"
                )

            except Exception as e:

                failed += 1

                error_message = str(e)

                print(
                    f"⚠️ Skipped : {Path(file_path).name}"
                )

                print(
                    f"   Reason : {error_message}"
                )

                errors.append(
                    f"{Path(file_path).name} -> {error_message}"
                )

                try:

                    self.dataset_repository.update_status(

                        file_path=file_path,

                        status="failed"

                    )

                except Exception:

                    pass

                continue

        return AgentResult(

            agent_name=self.agent_name,

            status=AgentStatus.COMPLETED,

            started_at=self.started_at,

            finished_at=datetime.now(),

            records_processed=processed,

            success=(failed == 0),

            message=(

                f"Processed={processed}, "

                f"Failed={failed}, "

                f"Skipped={skipped}"

            ),

            data={

                "processed": processed,

                "failed": failed,

                "skipped": skipped

            },

            errors=errors

        )


# ==========================================================
# Standalone Execution
# ==========================================================

if __name__ == "__main__":

    agent = CleaningAgent()

    agent.run()