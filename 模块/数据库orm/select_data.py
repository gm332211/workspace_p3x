from create_tables import engine
from create_tables import User
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
#查询所有 .all查询出一个列表，first查询出一个对象
session.query(User).filter().all()
#条件查询
session.query(User).filter(User.id==1).all()
#字段查询
session.query(User.name).filter(User.id==1).all()
#多条件查询
data=session.query(User).filter(User.id==1).filter(User.name.in_(['xiaoming',])).all()
#like查询
session.query(User).filter(User.name.like("xiaom%")).all()
#all查看
print(data[0].name)
#first()查看
# print(data.name)
