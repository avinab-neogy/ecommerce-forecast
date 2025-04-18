from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

def train_sarima(train_data: pd.Series, product_id: str):
    # Example config - tune using grid search
    order = (1, 1, 1)
    seasonal_order = (1, 1, 1, 7)  # Weekly seasonality
    
    model = SARIMAX(
        train_data,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=False
    )
    fitted_model = model.fit(disp=False)
    
    # Save model to MinIO
    fitted_model.save(f"/opt/airflow/models/sarima_{product_id}.pkl")
