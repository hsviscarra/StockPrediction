import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import os


def generate_report():
    ref_path = os.path.join("data", "reference.csv")
    cur_path = os.path.join("data", "current.csv")
    report_path = "report.html"

    if os.path.exists(ref_path) and os.path.exists(cur_path):
        ref = pd.read_csv(ref_path)
        cur = pd.read_csv(cur_path)
        report = Report(metrics=[DataDriftPreset()])
        report.run(reference_data=ref, current_data=cur)
        report.save_html(report_path)
        print("✅ Report generated successfully.")
    else:
        print("⚠️  reference.csv or current.csv not found.")
