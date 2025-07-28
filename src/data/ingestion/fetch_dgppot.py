from datetime import date
import os
import pandas_datareader.data as pdr


# Task function: Fetch GDPPOT data from FRED
def fetch_gdppot_data():
    end = date.today()
    print(
        f"""Year = {end.year};
month = {end.month};
day = {end.day}"""
    )

    # Avoid errors if today is Feb 29 (not every year has it)
    try:
        start = date(year=end.year - 70, month=end.month, day=end.day)
    except ValueError:
        start = date(year=end.year - 70, month=end.month, day=1)  # fallback to day 1

    print(f"Fetching FRED GDPPOT data from {start} to {end}...")

    df = pdr.DataReader("GDPPOT", "fred", start=start)

    if df.empty:
        raise ValueError("No GDPPOT data returned from FRED")

    os.makedirs("/opt/airflow/data", exist_ok=True)
    output_path = "/opt/airflow/data/gdppot.csv"
    df.to_csv(output_path)
    print(f"✅ GDPPOT data saved to {output_path}")
