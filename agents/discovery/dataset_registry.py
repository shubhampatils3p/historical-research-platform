"""
dataset_registry.py

Version : 2.0.0

Registers all local datasets into DuckDB.
"""

from pathlib import Path
from datetime import datetime

from agents.base.base_agent import BaseAgent, AgentResult, AgentStatus
from config.storage_contract import RAW_DATA
from database.repositories.dataset_repository import DatasetRepository


SUPPORTED_EXTENSIONS = {
    ".csv",
    ".parquet",
    ".xlsx",
    ".json",
    ".feather"
}


class DatasetRegistryAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.repository = DatasetRepository()

    # ---------------------------------------------------------

    def execute(self):

        datasets_found = 0
        registered = 0

        for file in RAW_DATA.rglob("*"):

            if not file.is_file():
                continue

            if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            datasets_found += 1

            if self.repository.dataset_exists(str(file)):
                continue

            stat = file.stat()

            self.repository.insert_dataset(

                dataset_name=file.stem,

                file_name=file.name,

                file_path=str(file),

                extension=file.suffix.lower(),

                size_bytes=stat.st_size,

                created_at=datetime.fromtimestamp(
                    stat.st_ctime
                ),

                modified_at=datetime.fromtimestamp(
                    stat.st_mtime
                ),

                status="registered"

            )

            registered += 1

        return AgentResult(

            agent_name=self.agent_name,

            status=AgentStatus.COMPLETED,

            started_at=self.started_at,

            finished_at=datetime.now(),

            records_processed=registered,

            success=True,

            message=f"{registered} datasets registered.",

            data={
                "datasets_found": datasets_found,
                "registered": registered
            }

        )