import shap

def explain_model(model, sample_data):
    # For tree-based models
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(sample_data)
    
    # Save visualization
    shap.summary_plot(shap_values, sample_data, show=False)
    plt.savefig('/opt/airflow/reports/shap_summary.png')
