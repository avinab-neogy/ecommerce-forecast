FROM apache/airflow:2.6.3
COPY requirements.txt /
USER airflow
RUN pip install --no-cache-dir -r /requirements.txt
