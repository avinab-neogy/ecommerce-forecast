def ingest_task():
    import pandas as pd
    from scripts.ingest import load_to_postgres, archive_to_minio

    # Read sample data
    df = pd.read_csv('/opt/airflow/data/sample_sales.csv')
    load_to_postgres(df, 'sales_data')
    archive_to_minio('/opt/airflow/data/sample_sales.csv', 'raw-data')
