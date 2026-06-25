"""
reader_factory.py

Version : 1.0.0

Reader Factory

Creates the appropriate reader based on file extension.

Author:
Chief Architect
"""

from pathlib import Path

from readers.csv_reader import CSVReader


class ReaderFactory:
    """
    Factory responsible for creating
    the correct reader for a file.
    """

    _READERS = {
        ".csv": CSVReader,
    }

    @classmethod
    def register_reader(cls, extension: str, reader_class):
        """
        Register a new reader.

        Example:
            ReaderFactory.register_reader(".parquet", ParquetReader)
        """

        cls._READERS[extension.lower()] = reader_class

    @classmethod
    def get_reader(cls, file_path):

        file_path = Path(file_path)

        extension = file_path.suffix.lower()

        if extension not in cls._READERS:

            raise ValueError(
                f"No reader registered for extension: {extension}"
            )

        return cls._READERS[extension](file_path)

    @classmethod
    def supported_extensions(cls):

        return list(cls._READERS.keys())