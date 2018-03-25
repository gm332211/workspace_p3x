class school(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.teachers=[] #类中关系的连接
        self.students=[]
    def registry(self,obj):
        print('%s学校招到了%s学生'%(self.name,obj.name))
        self.students.append(obj)
    def entry(self,obj):
        print('%s 成为了%s的教师'%(obj.name,self.name))
        self.teachers.append(obj)
class schoolmember(object): #类的继承,提取共同的特性
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
class student(schoolmember):
    def __init__(self,name,age,sex,course):
        super(student,self).__init__(name,age,sex)
        self.course=course
    def listen_class(self):
        print('%s 正在听%s课程'%(self.name,self.course))
class teacher(schoolmember):
    def __init__(self,name,age,sex,make_class):
        super(teacher,self).__init__(name,age,sex)
        self.make_class=make_class
    def in_class(self):
        print('%s 上正上%s课程'%(self.name,self.make_class))
sc1=school('职教','江苏盐城')
stu1=student('xiaoming',22,'F','python')
sc1.registry(stu1)
tea1=teacher('lilaoshi',30,'F','java')
sc1.entry(tea1)
stu1.listen_class()
tea1.in_class()
