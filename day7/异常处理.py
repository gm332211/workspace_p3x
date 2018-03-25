try:
    name['xiaoming']
except ValueError as e:
    print(e)
except NameError as e: #抓取单独错误
    print('没有这个key',e)
except Exception as e: #抓取所有错误
    print('未知错误',e)
else: #没有错误
    print('一切正常')
finally:
    print('我都执行')
#自定义错误
class mysqlconnectfailure(Exception):
    '''自定义错误类'''
    def __init__(self,msg):
        self.message=msg
    def __str__(self):
        return self.message
try:
     raise mysqlconnectfailure('数据库连接失败')
except mysqlconnectfailure as e:
    print(e)