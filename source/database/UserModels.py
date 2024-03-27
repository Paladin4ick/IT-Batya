from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Users(Base):
    __tablename__ = "AnyUser"
    user_id = Column(Integer)
    user_first_name = Column(String)
    user_full_name = Column(String)
    
 