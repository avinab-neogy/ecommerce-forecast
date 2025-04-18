from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='test_dag_2',
    start_date=datetime(2025, 4, 16),
    schedule_interval=None,
    catchup=False
) as dag:
    task_echo = BashOperator(
        task_id='echo_message',
        bash_command='echo "This is test DAG 2"'
    )
