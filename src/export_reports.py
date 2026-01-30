import os
import matplotlib.pyplot as plt
from utils import get_env, log

def export_reports(df):
    out = get_env("OUTPUT_DIR", "./reports")
    os.makedirs(out, exist_ok=True)
    current = os.path.join(out, "current_costs.csv")
    sim = os.path.join(out, "simulated_savings.csv")

    df.to_csv(sim, index=False)
    log(f"Reports exported: {sim}")

    plt.figure(figsize=(10,5))
    plt.bar(df["bucket"], df["current_cost"], label="Current")
    plt.bar(df["bucket"], df["it_cost"], label="Intelligent-Tiering")
    plt.bar(df["bucket"], df["glacier_cost"], label="Glacier")
    plt.xticks(rotation=45, ha="right")
    plt.title("S3 Cost Simulation per Bucket")
    plt.ylabel("USD")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(out, "savings_chart.png"))
    log("Savings chart saved.")
