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

            dataset_name TEXT,

            validation_time TIMESTAMP,

            validation_status TEXT,

            total_records INTEGER,

            passed_records INTEGER,

            failed_records INTEGER,

            warning_records INTEGER,

            duplicate_records INTEGER,

            null_records INTEGER,

            total_issues INTEGER,

            report_path TEXT

        )

    """,
    
    "cleaning_results": """

        CREATE TABLE IF NOT EXISTS cleaning_results (

            file_path TEXT PRIMARY KEY,

            cleaned_at TIMESTAMP,

            cleaning_status TEXT,

            rows_before INTEGER,

            rows_after INTEGER,

            duplicates_removed INTEGER,

            null_rows_removed INTEGER,

            null_columns_removed INTEGER,

            columns_standardized INTEGER,

            data_types_converted INTEGER,

            output_path TEXT

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