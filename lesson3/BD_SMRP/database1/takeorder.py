from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from BD_SMRP.database1.base_meta1 import Base


class Takeorder(Base):
    __tablename__ = 'TakeOrder'
    __table_args__ = {'extend_existing': True}

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    seller_id = Column(Integer, ForeignKey('Seller.id'), nullable=False)
    buyer_id = Column(Integer, ForeignKey('Buyer.id'), nullable=False)
    pvz_id = Column(Integer, ForeignKey('PVZ.id'), nullable=False)
    status = Column(Text(15), nullable=False)

    seller = relationship("Seller", back_populates="takeorder3")
    buyer = relationship("Buyer", back_populates="takeorder2")
    pvz = relationship("PVZ", back_populates="takeorder1")

    def __str__(self):
        return f"Заказ {self.order_id}: {self.seller.ProductName} {self.seller.ProductPrice} {self.buyer.FirstName} {self.buyer.SecondName} {self.pvz.id}"