import pandas as pd


# ------------------------------
# Load dataset
# ------------------------------
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


# ------------------------------
# Target binning only
# ------------------------------
def create_targets(df: pd.DataFrame):
    def bin_stress(x):
        if x <= 4:
            return "Low"
        elif x <= 7:
            return "Medium"
        else:
            return "High"

    def bin_sleep(x):
        return "Poor" if x <= 5 else "Good"

    df["Stress_Class"] = df["Stress Level"].apply(bin_stress)
    df["Sleep_Class"] = df["Quality of Sleep"].apply(bin_sleep)

    return df