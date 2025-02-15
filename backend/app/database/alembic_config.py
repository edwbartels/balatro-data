from dotenv import load_dotenv
import os

load_dotenv()


def get_url():
    return os.getenv("DATABASE_URL")
