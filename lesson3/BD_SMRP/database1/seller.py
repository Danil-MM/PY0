from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from BD_SMRP.database1.base_meta1 import Base


class Seller(Base):
    __tablename__ = 'Seller'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True )
    name = Column(Text(50), nullable=False)
    ProductName = Column(Text(50), nullable=False)
    ProductPrice = Column(Integer, nullable=False)
    takeorder3 = relationship("Takeorder", back_populates="seller")


    def __str__(self):
       return f"Продавец {self.id}: {self.name} {self.ProductName} {self.ProductPrice}"
