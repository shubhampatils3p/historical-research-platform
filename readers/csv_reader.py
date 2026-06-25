"""
csv_reader.py

Version : 1.0.0

CSV Reader

Author:
Chief Architect
"""

from pathlib import Path

import pandas as pd

from readers.base_reader import BaseReader, ReaderResult


class CSVReader(BaseReader):
    """
    Reads CSV datasets.
    """

    SUPPORTED_EXTENSIONS = [".csv"]

    def __init__(self, file_path: Path):

        super().__init__(file_path)

    # ---------------------------------------------------------

    def read(self) -> ReaderResult:

        self.validate_extension()

        try:

            dataframe = pd.read_csv(
                self.file_path,
                low_memory=False
            )

        except pd.errors.EmptyDataError:

            raise ValueError(
                f"Dataset is empty: {self.file_path}"
            )

        return self.build_result(
            dataframe=dataframe,
            message="CSV loaded successfully."
        )