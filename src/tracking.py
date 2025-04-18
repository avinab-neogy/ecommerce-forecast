import mlflow

def track_experiment(params: dict, metrics: dict):
    mlflow.set_tracking_uri("http://mlflow-server:5000")
    mlflow.set_experiment("ecommerce-forecast")
    
    with mlflow.start_run():
        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.log_artifact("model.pkl")  # Log trained model
