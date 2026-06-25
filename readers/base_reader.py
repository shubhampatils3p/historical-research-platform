"""
base_reader.py

Version : 1.0.0

Base Reader for Historical Research Platform.

Every file reader must inherit from this class.

Supported readers:
- CSV
- Parquet
- Excel
- JSON
- Feather
- DuckDB (future)

Author:
Chief Architect
"""

from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, Optional

import pandas as pd
from pydantic import BaseModel, ConfigDict


# ==========================================================
# READER RESULT
# ==========================================================

class ReaderResult(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        arbitrary_types_allowed=True
    )

    success: bool

    file_path: str

    file_type: str

    rows: int

    columns: int

    column_names: list[str]

    dataframe: Optional[pd.DataFrame] = None

    metadata: Dict[str, Any] = {}

    message: str = ""


# ==========================================================
# BASE READER
# ==========================================================

class BaseReader(ABC):

    """
    Base class for every file reader.
    """

    SUPPORTED_EXTENSIONS: list[str] = []

    def __init__(self, file_path: Path):

        self.file_path = Path(file_path)

        self.started_at: Optional[datetime] = None

        self.finished_at: Optional[datetime] = None

    # -----------------------------------------------------

    def exists(self) -> bool:

        return self.file_path.exists()

    # -----------------------------------------------------

    def file_size(self) -> int:

        return self.file_path.stat().st_size

    # -----------------------------------------------------

    @abstractmethod
    def read(self) -> ReaderResult:
        """
        Read file and return ReaderResult.
        """
        pass

    # -----------------------------------------------------

    def validate_extension(self):

        if self.file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:

            raise ValueError(
                f"{self.file_path.suffix} is not supported by "
                f"{self.__class__.__name__}"
            )

    # -----------------------------------------------------

    def build_result(
        self,
        dataframe: pd.DataFrame,
        message: str = ""
    ) -> ReaderResult:

        return ReaderResult(

            success=True,

            file_path=str(self.file_path),

            file_type=self.file_path.suffix.lower(),

            rows=len(dataframe),

            columns=len(dataframe.columns),

            column_names=list(dataframe.columns),

            dataframe=dataframe,

            metadata={

                "file_size_bytes": self.file_size(),

                "created_at": datetime.fromtimestamp(
                    self.file_path.stat().st_ctime
                ).isoformat(),

                "modified_at": datetime.fromtimestamp(
                    self.file_path.stat().st_mtime
                ).isoformat()

            },

            message=message
        )