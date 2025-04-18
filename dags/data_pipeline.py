from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# ---- Critical Fix: Add Scripts Directory to Python Path ---- 
# Get absolute path to dags directory
dag_dir = os.path.dirname(__file__)
# Navigate up to project root (../ from dags/)
project_root = os.path.abspath(os.path.join(dag_dir, ".."))
# Add scripts directory explicitly
scripts_path = os.path.join(project_root, "scripts")
sys.path.insert(0, scripts_path)

# Import AFTER path modification
from ingest import ingest_task  # Now directly from scripts/

# ---- DAG Configuration ----
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'ecommerce_data_pipeline',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,  # Manual trigger
    catchup=False
) as dag:
    ingest_operator = PythonOperator(
        task_id='ingest_raw_data',
        python_callable=ingest_task
    )
