from peewee import PostgresqlDatabase
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
import os

load_dotenv()

url = urlparse(os.getenv("DATA_BASE_URL", ""))

query_params = {k: v[0] for k, v in parse_qs(url.query).items()}

db = PostgresqlDatabase(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
    **query_params
)