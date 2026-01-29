import pandas as pd
from utils import get_env, log

def simulate_lifecycle(df):
    std_rate = float(get_env("STANDARD_RATE"))
    glacier_rate = float(get_env("GLACIER_RATE"))
    it_rate = float(get_env("INTELLIGENT_TIER_RATE"))

    df["current_cost"] = df["size_gb"] * std_rate
    df["it_cost"] = df["size_gb"] * it_rate
    df["glacier_cost"] = df["size_gb"] * glacier_rate

    df["savings_it"] = df["current_cost"] - df["it_cost"]
    df["savings_glacier"] = df["current_cost"] - df["glacier_cost"]

    total = df[["savings_it", "savings_glacier"]].sum().round(2)
    log(f"Simulated savings — IT: ${total.savings_it}, Glacier: ${total.savings_glacier}")
    return df
