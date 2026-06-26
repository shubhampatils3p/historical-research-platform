"""
base_writer.py

Base writer interface.
"""

from abc import ABC, abstractmethod


class BaseWriter(ABC):

    @abstractmethod
    def write(
        self,
        dataframe,
        output_path
    ):
        pass