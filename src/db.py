from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass

_engine = None
_Session = None

def init_engine(url: str):
    global _engine, _Session
    _engine = create_engine(url, pool_pre_ping=True)
    _Session = sessionmaker(bind=_engine)
    return _engine

def get_session():
    return _Session()
    