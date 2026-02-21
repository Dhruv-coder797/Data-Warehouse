import subprocess
from datetime import datetime
import os
import sys
# project root path automatically detect
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ensure logs folder exists
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
subprocess.run(
    [sys.executable, os.path.join(BASE_DIR, "scripts/init_db.py")],
    check=True
)
log_file = os.path.join(BASE_DIR, "logs/pipeline.log")
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
