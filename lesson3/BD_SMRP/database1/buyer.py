from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from BD_SMRP.database1.base_meta1 import Base


class Buyer(Base):
    __tablename__ = 'Buyer'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    FirstName = Column(Text(50), primary_key=False)
    SecondName = Column(Text(50), primary_key=False)
    takeorder2 = relationship("Takeorder", back_populates="buyer")

    def __str__(self):
      return f"Покупатель {self.id}: {self.FirstName} {self.SecondName}"
