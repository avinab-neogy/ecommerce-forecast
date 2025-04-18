from prophet import Prophet
import pandas as pd

def train_prophet(train_df: pd.DataFrame):
    # Prepare data (Prophet requires 'ds' and 'y' columns)
    df = train_df.rename(columns={'date': 'ds', 'quantity': 'y'})
    
    model = Prophet(
        weekly_seasonality=True,
        daily_seasonality=False
    )
    
    # Add external regressors (e.g., price, promotions)
    if 'temperature' in train_df.columns:
        model.add_regressor('temperature')
    
    model.fit(df)
    
    # Save model
    from joblib import dump
    dump(model, '/opt/airflow/models/prophet_model.joblib')
