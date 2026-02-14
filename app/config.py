import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")
HF_TOKEN = os.getenv("HF_TOKEN")