from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from BD_SMRP.database1.base_meta1 import Base


class PVZ(Base):
    __tablename__ = 'PVZ'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True )
    city = Column(Text(50), primary_key=False)
    street = Column(Text(50), primary_key=False)
    takeorder1 = relationship("Takeorder", back_populates="pvz")

    def __str__(self):
      return f"Пункт_выдачи {self.id}: {self.city} {self.street}"
