"""
Historical Research Platform

Main Entry Point

Responsibilities
----------------
1. Initialize database
2. Run Dataset Registry Agent
3. Run Dataset Inspector Agent
"""

from database.database_manager import DatabaseManager

from agents.discovery.dataset_registry import DatasetRegistryAgent
from agents.inspection.dataset_inspector import DatasetInspectorAgent


def initialize():

    print("=" * 60)
    print("HISTORICAL RESEARCH PLATFORM")
    print("=" * 60)

    # ------------------------------------------------------
    # Database Initialization
    # ------------------------------------------------------

    db = DatabaseManager()

    db.create_tables()

    print("✅ Database Initialized")

    # ------------------------------------------------------
    # Dataset Registry
    # ------------------------------------------------------

    print("\n🚀 Running Dataset Registry Agent...")

    DatasetRegistryAgent().run()

    # ------------------------------------------------------
    # Dataset Inspection
    # ------------------------------------------------------

    print("\n🚀 Running Dataset Inspector Agent...")

    DatasetInspectorAgent().run()

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED")
    print("=" * 60)


if __name__ == "__main__":

    initialize()