#Currently just testing SQL functions using python
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv(".env")


db = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER_NAME"),
    passwd = os.getenv("DB_USER_PWD"),
)

db.autocommit = True
mycursor = db.cursor()
