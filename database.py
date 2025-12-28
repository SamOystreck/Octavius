#Currently just testing SQL functions using python
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_MODIFIER_NAME"),
    passwd = os.getenv("DB_MODIFIER_PWD"),
)

db.autocommit = True
mycursor = db.cursor()
