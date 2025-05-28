from sqlalchemy import column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    
    id = column(Integer, primary_key=True, index=True)
    name = column(String, index=True)
    email = column(String, unique=True, index=True)
    created_at = column(String, default=datetime.utcnow().isoformat())

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"