from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
engine=create_engine('mysql+pymysql://root:password@172.24.2.10/py3_test',encoding='utf-8',echo=True)
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String(64))
    password=Column(String(64))
Base.metadata.create_all(engine)

