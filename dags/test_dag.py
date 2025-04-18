from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='test_dag',
    start_date=datetime(2025, 4, 16),
    schedule_interval=None,
    catchup=False
) as dag:
    task_hello = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello, Airflow!"'
    )
