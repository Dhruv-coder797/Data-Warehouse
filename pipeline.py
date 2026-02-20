import subprocess
from datetime import datetime

log_file = "logs/pipeline.log"
error_file = "logs/error.log"

def log(message):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} : {message}\n")

def error(message):
    with open(error_file, "a") as f:
        f.write(f"{datetime.now()} : {message}\n")

log("Pipeline STARTED")

try:
    subprocess.run(
        ["python3", "scripts/load_staging.py"],
        check=True
    )

    subprocess.run(
        ["python3", "scripts/run_transform.py"],
        check=True
    )

    log("Pipeline SUCCESS")

except Exception as e:
    error(f"Pipeline FAILED → {e}")
    log("Pipeline FAILED")
