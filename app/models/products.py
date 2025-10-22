from app.database.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String,DateTime,Integer
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from typing import List


class Product(Base):
    __tablename__ = "product"
    
    product_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    insert_date: Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    product_name: Mapped[str] = mapped_column(String(200))
    product_url: Mapped[str] = mapped_column(String(200))
    store_id: Mapped[int] = mapped_column(Integer,ForeignKey("store.store_id"))
    
    store: Mapped["Store"] = relationship(back_populates="products")
    
    prices: Mapped[List["Price"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )
    
    