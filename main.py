"""
Historical Research Platform

Main Entry Point

Responsibilities
----------------
1. Initialize database
2. Run Dataset Registry Agent
3. Run Dataset Inspector Agent
4. Run Validation Agent
"""

from database.database_manager import DatabaseManager

from agents.discovery.dataset_registry import DatasetRegistryAgent
from agents.inspection.dataset_inspector import DatasetInspectorAgent
from agents.validation.validation_agent import ValidationAgent
from agents.cleaning.cleaning_agent import CleaningAgent

# ==========================================================
# Agent Runner
# ==========================================================

def run_agent(title: str, agent):

    print(f"\n🚀 Running {title}...")

    agent.run()


# ==========================================================
# Initialize Platform
# ==========================================================

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
    # Pipeline
    # ------------------------------------------------------

    run_agent(
        "Dataset Registry Agent",
        DatasetRegistryAgent()
    )

    run_agent(
        "Dataset Inspector Agent",
        DatasetInspectorAgent()
    )

    run_agent(
        "Validation Agent",
        ValidationAgent()
    )
    
    run_agent(
        "Cleaning Agent",
        CleaningAgent()
    )

    # ------------------------------------------------------

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED")
    print("=" * 60)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    initialize()