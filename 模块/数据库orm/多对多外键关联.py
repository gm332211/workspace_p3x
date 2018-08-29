from create_tables import engine,User,Address,BranchSchool,Teacher,Course,Class_g
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(engine)
session=Session()

# #创建地址
# a1=Address(city='无锡',addr='钱胡路809号')
# a2=Address(city='无锡',addr='6A-401')
# a3=Address(city='盐城',addr='江苏盐城射阳')
# #创建学校
# s1=BranchSchool(name='无锡商业职业技术学院',addr=a1)
# #创建学校课程
# course1=Course(name='python')
# course2=Course(name='java')
# course3=Course(name='web')
# course4=Course(name='mysql')
# course5=Course(name='H3C')
# course6=Course(name='CAD')
# course7=Course(name='PS')
# course8=Course(name='OpenStack')
# #创建班级
# c1=Class_g(name='计算机网络142',school=s1,course=[course1,course7,course6,course4])
# c2=Class_g(name='计算机网络141',school=s1,course=[course2,course3,course5,course8])
# #创建教师
# t1=Teacher(name='张飞',course=[course1,course3,course5],class_g=[c1])
# t2=Teacher(name='王五',course=[course1,course2,course5,course7],class_g=[c1,c2])
# t3=Teacher(name='李四',course=[course4,course3,course7],class_g=[c2])
# t4=Teacher(name='王二',course=[course2,course3,course8],class_g=[c1])
# t5=Teacher(name='古六',course=[course6])
# #创建学生
# u1=User(name='小明',password='12345',class_g=c1,school=s1,home_address=a3,dorm_address=a2)
# u2=User(name='小明',password='test',class_g=c2,school=s1,home_address=a3,dorm_address=a2)
# session.add_all([
# a1,a2,a3,s1,course1,course2,course3,course4,course5,course6,course7,course8,c1,c2,t1,t2,t3,t4,t5,u1,u2
# ])
# session.commit()
#查询

data=session.query(BranchSchool).filter(BranchSchool.name.like('无锡%')).first()
print(data)
print(data.user)
print(data.class_g)
for class_one in data.class_g:
    print(class_one.name,'course:',class_one.course)
    print(class_one.name, 'teacher:',class_one.teacher,'student:',class_one.user)
