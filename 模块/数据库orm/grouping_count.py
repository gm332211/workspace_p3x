from create_tables import engine,User
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
#计数
session.query(User).filter(User.name.like("xiao%")).count()
#分组计数
count=session.query(User.name,func.count(User.name)).group_by(User.name).all()
print(count)