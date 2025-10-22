from app.database.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String,DateTime,Integer
from datetime import datetime
from typing import List
from sqlalchemy.orm import relationship

class Store(Base):
    __tablename__ = "store"
    
    store_id:Mapped[int] = mapped_column(Integer,primary_key=True)
    insert_date: Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    store_name: Mapped[str] = mapped_column(String(100))
    
    products: Mapped[List["Product"]] = relationship(
        back_populates="store",
        cascade="all, delete-orphan"
    )
