from sqlalchemy import create_engine
from app.database.Base import Base
from app.models.price import Price
from app.models.products import Product
from app.models.store import Store

import sqlite3


conn = sqlite3.connect('EstoreMonitoring.db')
cur = conn.cursor()

DB_URL = 'sqlite:///EstoreMonitoring.db'

engine = create_engine(DB_URL,echo =  True)

Base.metadata.create_all(engine)