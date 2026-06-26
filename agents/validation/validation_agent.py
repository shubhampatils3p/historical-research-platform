"""
validation_agent.py

Version : 1.0.0

Dataset Validation Agent

Responsibilities
----------------
1. Read inspected datasets
2. Validate datasets
3. Save validation results
4. Update dataset status
5. Generate validation reports
"""

from datetime import datetime
from pathlib import Path

from agents.base.base_agent import (
    BaseAgent,
    AgentResult,
    AgentStatus,
)

from readers.reader_factory import ReaderFactory

from agents.validation.validation_rules import ValidationRules
from agents.validation.validation_report import ValidationReport

from database.repositories.dataset_repository import DatasetRepository
from database.repositories.validation_repository import ValidationRepository


class ValidationAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.dataset_repository = DatasetRepository()

        self.validation_repository = ValidationRepository()

    # ==========================================================
    # Validate Single Dataset
    # ==========================================================

    def validate_dataset(
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
        # Validate Dataset
        # ------------------------------------------------------

        validation_result = ValidationRules.validate_dataset(

            dataframe,

            dataset_name=file_path.stem

        )

        # ------------------------------------------------------
        # Generate Reports
        # ------------------------------------------------------

        report = ValidationReport()

        txt_report = report.save_txt(
            validation_result
        )

        report.save_json(
            validation_result
        )

        # ------------------------------------------------------
        # Save Validation Result
        # ------------------------------------------------------

        self.validation_repository.save_result(

            dataset_name=validation_result.dataset_name,

            file_path=str(file_path),

            validation_time=validation_result.validation_time,

            validation_status=validation_result.status.value,

            total_records=validation_result.summary.total_records,

            passed_records=validation_result.summary.passed_records,

            failed_records=validation_result.summary.failed_records,

            warning_records=validation_result.summary.warning_records,

            duplicate_records=validation_result.summary.duplicate_records,

            null_records=validation_result.summary.null_records,

            total_issues=len(validation_result.issues),

            report_path=str(txt_report)

        )

        # ------------------------------------------------------
        # Update Dataset Registry
        # ------------------------------------------------------

        self.dataset_repository.mark_validated(

            str(file_path)

        )

        return validation_result
    
    # ==========================================================
    # Execute
    # ==========================================================

    def execute(self):

        datasets = self.dataset_repository.get_inspected_datasets()

        processed = 0
        failed = 0
        skipped = 0

        errors = []

        for row in datasets:

            file_path = row[0]

            try:

                self.validate_dataset(file_path)

                processed += 1

                print(
                    f"✅ Validated : {Path(file_path).name}"
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

    agent = ValidationAgent()

    agent.run()