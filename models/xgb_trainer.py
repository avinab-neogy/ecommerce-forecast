from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline

def train_xgboost(X_train, y_train):
    model = XGBRegressor(
        objective='reg:squarederror',
        tree_method='gpu_hist',  # GPU acceleration
        n_estimators=1000,
        max_depth=8,
        learning_rate=0.1
    )
    
    pipeline = Pipeline([
        ('preprocessor', your_preprocessing_steps),
        ('model', model)
    ])
    
    pipeline.fit(X_train, y_train)
    return pipeline
