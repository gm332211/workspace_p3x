from sqlalchemy import create_engine,Column,Integer,String,Date,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base=declarative_base()
engine=create_engine('mysql+pymysql://root:password@172.24.2.10/py3_test',encoding='utf-8',echo=False)
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String(64))
    password=Column(String(64))
    #创建多外键关联外键
    home_address_id=Column(Integer,ForeignKey('address.id'),default=None)
    school_address_id=Column(Integer,ForeignKey('address.id'),default=None)
    #多外键关联反射
    home_address=relationship('Address',backref='home_address',foreign_keys=[home_address_id])
    school_address=relationship('Address',backref='school_address',foreign_keys=[school_address_id])
    def __repr__(self):
        #可视化显示
        return '<%s home_addr:%s school_addr:%s>' % (self.name, self.home_address.name, self.school_address.name)
class Address(Base):
    __tablename__='address'
    id=Column(Integer,primary_key=True)
    name=Column(String(128))
    def __str__(self):
        return self.name
    def __repr__(self):
        return '<%s>'%self.name
class UserRecode(Base):
    __tablename__='user_recode'
    id=Column(Integer,primary_key=True)
    day=Column(Date)
    status=Column(String(32),default='NO')
    #外键关联
    user_id=Column(Integer,ForeignKey('user.id'))
    #反向查询该表
    user=relationship('User',backref='user_recode')
    def __repr__(self):
        return '<%s day:%s status:%s>'%(self.user.name,self.day,self.status)
Base.metadata.create_all(engine)

