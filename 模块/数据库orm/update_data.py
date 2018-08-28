from create_tables import engine
from create_tables import User
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
data=session.query(User).filter(User.id==1).all()
if data:
    #修改一条数据
    data[0].name='test'
    data[0].password='password123'
    session.commit()