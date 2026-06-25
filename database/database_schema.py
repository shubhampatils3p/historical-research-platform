"""
database_schema.py

Database Schema Definitions

Single Source of Truth for all database tables.

Author:
Chief Architect
"""

TABLES = {

    "dataset_registry": """

        CREATE TABLE IF NOT EXISTS dataset_registry (

            file_path TEXT PRIMARY KEY,

            dataset_name TEXT NOT NULL,

            file_name TEXT NOT NULL,

            extension TEXT,

            size_bytes BIGINT,

            created_at TIMESTAMP,

            modified_at TIMESTAMP,

            status TEXT,

            rows INTEGER,

            columns INTEGER,

            inspection_time TIMESTAMP,

            validation_time TIMESTAMP,

            cleaning_time TIMESTAMP,

            feature_generation_time TIMESTAMP

        )

    """,

    "inspection_results": """

        CREATE TABLE IF NOT EXISTS inspection_results (

            file_path TEXT PRIMARY KEY,

            inspected_at TIMESTAMP,

            row_count INTEGER,

            column_count INTEGER,

            missing_values INTEGER,

            duplicate_rows INTEGER,

            inspection_status TEXT,

            memory_mb DOUBLE,

            first_timestamp TIMESTAMP,

            last_timestamp TIMESTAMP

        )

    """,

    "validation_results": """

        CREATE TABLE IF NOT EXISTS validation_results (

            file_path TEXT PRIMARY KEY,

            validated_at TIMESTAMP,

            validation_status TEXT,

            error_count INTEGER,

            warning_count INTEGER

        )

    """,

    "feature_runs": """

        CREATE TABLE IF NOT EXISTS feature_runs (

            run_id TEXT PRIMARY KEY,

            started_at TIMESTAMP,

            finished_at TIMESTAMP,

            feature_version TEXT,

            status TEXT

        )

    """,

    "pipeline_runs": """

        CREATE TABLE IF NOT EXISTS pipeline_runs (

            run_id TEXT PRIMARY KEY,

            started_at TIMESTAMP,

            finished_at TIMESTAMP,

            agent_name TEXT,

            status TEXT,

            message TEXT

        )

    """

}