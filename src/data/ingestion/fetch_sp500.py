from datetime import date
import os
import pandas_datareader.data as pdr


def fetch_sp500_data():
    end = date.today()

    try:
        start = date(year=end.year - 5, month=end.month, day=end.day)
    except ValueError:
        start = date(year=end.year - 5, month=end.month, day=1)

    df = pdr.get_data_stooq("^SPX", start, end)

    if df.empty:
        raise ValueError("No SPX data returned")

    os.makedirs("/opt/airflow/data", exist_ok=True)
    output_path = "/opt/airflow/data/sp500.csv"
    df.to_csv(output_path)
    print(f"✅ SP500 data saved to {output_path}")
    return output_path
