from config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Movie(Base):

    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key = True)
    title = Column(String(length=100))
    overview = Column(String(length=100))
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String(length=100))