"""
csv_writer.py

CSV Writer
"""

from pathlib import Path

from writers.base_writer import BaseWriter


class CSVWriter(BaseWriter):

    def write(
        self,
        dataframe,
        output_path
    ):

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        dataframe.to_csv(

            output_path,

            index=False

        )

        return output_path