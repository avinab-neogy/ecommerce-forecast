import pandas as pd
from sqlalchemy import create_engine
from feature_engine.imputation import MeanMedianImputer
from feature_engine.creation import CyclicalFeatures
from sklearn.preprocessing import StandardScaler

POSTGRES_URI = "postgresql+psycopg2://airflow:airflow@postgres/airflow"

def run_feature_engineering():
    engine = create_engine(POSTGRES_URI)
    df = pd.read_sql("SELECT * FROM sales_features", engine)
    df['month'] = pd.to_datetime(df['date']).dt.month
    df['day_of_week'] = pd.to_datetime(df['date']).dt.dayofweek

    cyclical = CyclicalFeatures(variables=["month", "day_of_week"])
    imputer = MeanMedianImputer(imputation_method='median')
    scaler = StandardScaler()

    from sklearn.pipeline import Pipeline
    pipeline = Pipeline([
        ('cyclical', cyclical),
        ('impute', imputer),
        ('scale', scaler)
    ])
    processed = pipeline.fit_transform(df)
    processed_df = pd.DataFrame(processed, columns=df.columns)
    processed_df.to_parquet('/opt/airflow/data/processed_features.parquet')
