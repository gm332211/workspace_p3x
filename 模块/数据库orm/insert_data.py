from create_tables import engine,User
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
u1=User(name='xiaoming',password='12345')
#单条插入
session.add(u1)
#多条插入
session.add_all([u1,])
session.commit()