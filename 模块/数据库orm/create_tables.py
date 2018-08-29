from sqlalchemy import create_engine,Column,Integer,String,Date,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base=declarative_base()
engine=create_engine('mysql+pymysql://root:password@172.24.2.10/py3_test?charset=utf8',echo=False)
#多对多第三张表(多课程对教师)
teacher_m2m_course = Table('teacher_m2m_course',
                        Base.metadata, Column('teacher_id', Integer, ForeignKey('teacher.id')),
                        Base.metadata, Column('course_id', Integer, ForeignKey('course.id'))
                        )
#多对多第三张表(多课程对班级)
class_m2m_course = Table('class_m2m_course',
                        Base.metadata, Column('class_id', Integer, ForeignKey('class_g.id')),
                        Base.metadata, Column('course_id', Integer, ForeignKey('course.id'))
                        )
#多对多第三张表(多班级对教师)
teacher_m2m_class = Table('teacher_m2m_class',
                        Base.metadata, Column('teacher_id', Integer, ForeignKey('teacher.id')),
                        Base.metadata, Column('class_id', Integer, ForeignKey('class_g.id'))
                        )
class User(Base):
    #用户表
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String(64))
    password=Column(String(64))
    #单外键关联
    class_id=Column(Integer,ForeignKey('class_g.id'))
    school_id = Column(Integer,ForeignKey('branch_school.id'))
    #单外键反射
    class_g=relationship('Class_g',backref='user')
    school=relationship('BranchSchool',backref='user')
    #创建多外键关联外键
    home_address_id=Column(Integer,ForeignKey('address.id'),default=None)
    dorm_address_id=Column(Integer,ForeignKey('address.id'),default=None)
    #多外键关联反射
    home_address=relationship('Address',foreign_keys=[home_address_id])
    dorm_address=relationship('Address',foreign_keys=[dorm_address_id])
    #多对多关联
    def __repr__(self):
        #可视化显示
        return '<%s 班级:%s>' % (self.name, self.class_g.name)
class Address(Base):
    #地址表
    __tablename__='address'
    id=Column(Integer,primary_key=True)
    city=Column(String(128))
    addr=Column(String(128))
    def __repr__(self):
        return '<%s>'%self.addr

class Teacher(Base):
    #教师表
    __tablename__ = 'teacher'
    id=Column(Integer,primary_key=True)
    name=Column(String(128))
    course = relationship('Course', secondary=teacher_m2m_course, backref='teacher')
    class_g = relationship('Class_g', secondary=teacher_m2m_class, backref='teacher')
    def __repr__(self):
        return '<%s>'%self.name
class Course(Base):
    #课程表
    __tablename__='course'
    id=Column(Integer,primary_key=True)
    name=Column(String(128))
    def __repr__(self):
        return '<%s>'%self.name
class Class_g(Base):
    #班级表
    __tablename__='class_g'
    id=Column(Integer,primary_key=True)
    name=Column(String(128))
    school_id =Column(Integer,ForeignKey('branch_school.id'))
    school=relationship('BranchSchool',backref='class_g')
    course = relationship('Course', secondary=class_m2m_course, backref='class_g')
    def __repr__(self):
        return '<%s>'%(self.name)
class BranchSchool(Base):
    #学校表
    __tablename__ = 'branch_school'
    id=Column(Integer,primary_key=True)
    name = Column(String(128))
    addr_id=Column(Integer,ForeignKey('address.id'))
    addr=relationship('Address',backref='school')
    def __repr__(self):
        return '<%s>'%(self.name)


class UserRecode(Base):
    #状态记录表
    __tablename__='user_recode'
    id=Column(Integer,primary_key=True)
    day=Column(Date)
    status=Column(String(32),default='NO')
    #外键关联
    user_id=Column(Integer,ForeignKey('user.id'))
    course_id=Column(Integer,ForeignKey('course.id'))
    #反向查询该表
    user=relationship('User',backref='user_recode')
    course = relationship('Course', backref='user_recode')
    def __repr__(self):
        return '<%s day:%s status:%s>'%(self.user.name,self.day,self.status)
Base.metadata.create_all(engine)

