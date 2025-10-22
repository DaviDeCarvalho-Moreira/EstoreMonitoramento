from app.database.Base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Float,DateTime,Integer,String
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Price(Base):
    __tablename__ = "price"
    
    price_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    insert_date:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    price_avista: Mapped[float] = mapped_column(Float)
    price_parcelado: Mapped[float] = mapped_column(Float)
    product_id: Mapped[int] = mapped_column(Integer,ForeignKey("product.product_id"))
    
    product: Mapped["Product"] = relationship(back_populates="prices")
    
   