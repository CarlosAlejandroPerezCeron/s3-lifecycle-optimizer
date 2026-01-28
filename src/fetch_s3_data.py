import boto3
import pandas as pd
from utils import get_env, log

def fetch_s3_usage():
    client = boto3.client("s3", region_name=get_env("AWS_REGION"))
    s3 = boto3.resource("s3", region_name=get_env("AWS_REGION"))
    buckets = [b.name for b in s3.buckets.all()]
    log(f"Found {len(buckets)} buckets.")

    data = []
    for b in buckets:
        size_gb = 0
        bucket = s3.Bucket(b)
        for obj in bucket.objects.limit(500):  # límite para demo
            size_gb += obj.size / (1024**3)
        data.append({"bucket": b, "size_gb": round(size_gb, 2)})

    df = pd.DataFrame(data)
    log("Fetched S3 usage data.")
    return df
