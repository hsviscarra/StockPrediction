import pandas as pd
import numpy as np


def generate_sample_sp500_data():
    data = {
        "Date": pd.date_range(start="2024-01-01", periods=10),
        "Close": np.linspace(4000, 4050, 10),
    }
    return pd.DataFrame(data)
