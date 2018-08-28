from create_tables import engine,User,Address
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
#创建多外键关联
# a1=Address(name='YANCHENG')
# a2=Address(name='WUXI')
# u1=User(name='guming',password='admin',home_address=a1,school_address=a2)
# session.add_all([a1,a2,u1])
# session.commit()

data=session.query(User).all()
print(data)