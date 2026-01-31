from fetch_s3_data import fetch_s3_usage
from simulate_lifecycle import simulate_lifecycle
from export_reports import export_reports
from utils import log

def main():
    log("=== S3 Lifecycle Optimization Simulator ===")
    df = fetch_s3_usage()
    df = simulate_lifecycle(df)
    export_reports(df)
    log("Simulation complete.")

if __name__ == "__main__":
    main()
