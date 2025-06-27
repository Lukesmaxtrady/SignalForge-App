import pandas as pd

def export_audit_report(data: list, filename: str = "audit_report.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
