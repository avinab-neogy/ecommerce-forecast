# File: dags/feature_engineering.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=10),
    'execution_timeout': timedelta(minutes=60)
}

with DAG(
    'feature_engineering_pipeline',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,  # Manual trigger for now
    catchup=False,
    description='Advanced feature engineering and model tuning pipeline'
) as dag:
    
    # Task 1: Create SQL features using materialized view
    create_sql_features = PostgresOperator(
        task_id='create_sql_features',
        postgres_conn_id='postgres_conn',
        sql='/opt/airflow/sql/feature_views.sql',
        dag=dag
    )

    # Task 2: Python-based feature engineering
    def feature_engineering_task():
        from scripts.feature_engineer import run_feature_engineering
        run_feature_engineering()

    python_feature_engineering = PythonOperator(
        task_id='python_feature_engineering',
        python_callable=feature_engineering_task,
        dag=dag
    )

    # Task 3: Hyperparameter tuning
    def hyperparameter_tuning_task():
        from scripts.tune import run_tuning
        run_tuning()

    hyperparameter_tuning = PythonOperator(
        task_id='hyperparameter_tuning',
        python_callable=hyperparameter_tuning_task,
        dag=dag
    )

    # Set task dependencies
    create_sql_features >> python_feature_engineering >> hyperparameter_tuning
