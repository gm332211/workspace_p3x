from create_tables import engine
from create_tables import User
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
data=session.query(User).filter(User.id==1).filter(User.name.in_(['test',])).all()
if data:
    session.delete(data[0])
    session.commit()
