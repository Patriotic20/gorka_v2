from sqlalchemy import Column ,  String , Integer , DateTime
from src.base.db import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True , nullable=False )
    barcode = Column(String , nullable=False)
    name = Column(String , nullable=False)
    quantity = Column(Integer , nullable=False , default=0)
    create_at = Column(DateTime , default=datetime.utcnow , nullable=False)
    