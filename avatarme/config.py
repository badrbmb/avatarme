import os
from pathlib import Path

# root directory for dynamic path
ROOT_DIR = Path(__file__).parent.parent.resolve()

# data dir to store compute artifacts locally
DATA_DIR = ROOT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# default image dimension
DEFAULT_DIM = 512

# name of GCS bucket to store images
BUCKET_NAME = os.environ.get("BUCKET_NAME")
assert BUCKET_NAME is not None, ValueError("Env var `BUCKET_NAME` is not set!")
