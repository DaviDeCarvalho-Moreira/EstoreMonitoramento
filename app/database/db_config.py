from sqlalchemy import create_engine
import sqlite3


conn = sqlite3.connect('EstoreMonitoring.db')
cur = conn.cursor()

DB_URL = 'sqlite:///EstoreMonitoring.db'

engine = create_engine(DB_URL,echo =  True)