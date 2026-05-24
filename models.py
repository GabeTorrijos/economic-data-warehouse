from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class EconomicData(Base):
    __tablename__ = 'economic_data'

    id = Column(Integer, primary_key=True)
    series_id = Column(String, nullable=False)
    series_name = Column(String, nullable=False)
    date = Column(String, nullable=False)
    value = Column(Float, nullable=True)

    def __repr__(self):
        return f"<EconomicData(series_id={self.series_id}, date={self.date}, value={self.value})>"