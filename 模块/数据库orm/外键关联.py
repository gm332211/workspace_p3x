from create_tables import engine,User,UserRecode
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()
#创建用户
# u2=User(name='xiaoming1',password='12333445')
# u3=User(name='xiaoming2',password='12333445')
#创建状态表并关联用户
# r1=UserRecode(day='2018-01-02',status='Yes',user=u1)
# r2=UserRecode(day='2018-02-02',status='Yes',user=u2)
# r3=UserRecode(day='2018-03-02',user=u1)
# r4=UserRecode(day='2018-04-02',user=u1)
# r5=UserRecode(day='2018-05-02',status='Yes',user=u3)
#
# session.add_all([u1,u2,u3,r1,r2,r3,r4,r5])
# session.commit()
data=session.query(User).filter(User.name=='xiaoming1').first()
print(data)
print(data.user_recode)
