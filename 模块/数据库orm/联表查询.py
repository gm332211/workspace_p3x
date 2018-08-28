from create_tables import engine
from create_tables import User,UserRecode
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
session.query(User,UserRecode).filter(User.id==UserRecode.user_id).first()