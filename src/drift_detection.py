from evidently.report import Report
from evidently.metrics import DataDriftTable

def check_data_drift(current_data, reference_data):
    report = Report(metrics=[DataDriftTable()])
    report.run(
        current_data=current_data,
        reference_data=reference_data
    )
    report.save_html('/reports/data_drift.html')  # Save to shared volume
