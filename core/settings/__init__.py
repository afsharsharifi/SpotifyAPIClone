import os
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

from .base import *

if os.environ["ENV_NAME"] == "production":
    from .production import *
else:
    from .development import *
