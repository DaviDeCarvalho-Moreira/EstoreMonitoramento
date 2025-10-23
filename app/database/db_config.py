from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.Base import Base
from app.models.products import Product
from app.models.store import Store
import sqlite3


conn = sqlite3.connect('EstoreMonitoring.db')
cur = conn.cursor()

DB_URL = 'sqlite:///EstoreMonitoring.db'

engine = create_engine(DB_URL,echo =  True)

Session = sessionmaker(bind=engine)
session = Session()



Base.metadata.create_all(engine)

