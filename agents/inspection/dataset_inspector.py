"""
dataset_inspector.py

Version : 1.1.0

Dataset Inspector Agent

Responsibilities
----------------
1. Read dataset using ReaderFactory
2. Generate inspection summary
3. Save inspection results
4. Update dataset status
5. Generate inspection reports
"""

from datetime import datetime
from pathlib import Path

from agents.base.base_agent import (
    BaseAgent,
    AgentResult,
    AgentStatus,
)

from readers.reader_factory import ReaderFactory

from agents.inspection.inspection_rules import dataset_summary
from agents.inspection.inspection_report import InspectionReport

from database.repositories.dataset_repository import DatasetRepository
from database.repositories.inspection_repository import InspectionRepository


class DatasetInspectorAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.dataset_repository = DatasetRepository()
        self.inspection_repository = InspectionRepository()

    # ==========================================================
    # Inspect Single Dataset
    # ==========================================================

    def inspect(self, file_path: str):

        file_path = Path(file_path)

        # -----------------------------
        # Read Dataset
        # -----------------------------

        reader = ReaderFactory.get_reader(file_path)

        reader_result = reader.read()

        dataframe = reader_result.dataframe

        # -----------------------------
        # Generate Summary
        # -----------------------------

        summary = dataset_summary(dataframe)

        # -----------------------------
        # Save Inspection Result
        # -----------------------------

        self.inspection_repository.save_result(

            file_path=str(file_path),

            row_count=summary["rows"],

            column_count=summary["columns"],

            missing_values=summary["missing_values"],

            duplicate_rows=summary["duplicate_rows"],

            memory_mb=summary["memory_mb"],

            first_timestamp=summary["first_timestamp"],

            last_timestamp=summary["last_timestamp"],

            inspection_time=datetime.now()

        )

        # -----------------------------
        # Update Dataset Registry
        # -----------------------------

        self.dataset_repository.update_inspection(

            file_path=str(file_path),

            rows=summary["rows"],

            columns=summary["columns"]

        )

        # -----------------------------
        # Generate Reports
        # -----------------------------

        report = InspectionReport(summary)

        report_dir = Path("reports") / "inspection"

        report_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        report.save_text(
            report_dir / f"{file_path.stem}.txt"
        )

        report.save_json(
            report_dir / f"{file_path.stem}.json"
        )

        return summary

    # ==========================================================
    # Execute
    # ==========================================================

    def execute(self):

        datasets = self.dataset_repository.get_uninspected_datasets()

        processed = 0
        failed = 0
        skipped = 0
        errors = []

        for row in datasets:

            file_path = row[0]

            try:

                self.inspect(file_path)

                processed += 1

                print(f"✅ Inspected : {Path(file_path).name}")

            except Exception as e:

                failed += 1

                error_message = str(e)

                print(f"⚠️ Skipped : {Path(file_path).name}")

                print(f"   Reason : {error_message}")

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

            success= True,

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

    agent = DatasetInspectorAgent()

    agent.run()