"""
writer_factory.py

Writer Factory
"""

from pathlib import Path

from writers.csv_writer import CSVWriter


class WriterFactory:

    @staticmethod
    def get_writer(output_path):

        suffix = Path(output_path).suffix.lower()

        if suffix == ".csv":

            return CSVWriter()

        raise ValueError(

            f"Unsupported output format: {suffix}"

        )