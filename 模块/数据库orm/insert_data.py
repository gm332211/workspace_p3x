from create_tables import engine,User
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
u1=User(name='xiaoming',password='12345')
session.add(u1)
session.commit()