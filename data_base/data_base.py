from peewee import PostgresqlDatabase
from dotenv import load_dotenv
import os 

load_dotenv()

db = PostgresqlDatabase(os.getenv('DATA_BASE_URL', ''))
