#coding=utf-8
#Author:gm
fruit='cherry'

#字符串的判断
print('1.2'.isdigit())#判断是否是正整数
print('1a'.isalnum())#判断是否是数字和英文字母(不包含特殊字符)
print('1a'.isalpha())#判断是否是纯英文字符
print('1A'.isdecimal())#判断是否为十进制
print('1a'.isidentifier())#判断是不是合法的变量名
print('a1'.islower())#判断是否有小写
print(fruit.isnumeric())#判断是否是正整数
print(fruit.isprintable())#判断是否是打印文件
print(fruit.isspace())#判断是否是空格
print(fruit.istitle())#判断每个开头字母是否为大写
print(fruit.isupper())#判断是否为大写
print(fruit.endswith('ry'))#判断是否是'ry'结尾
print(fruit.startswith('ch'))#判断是否是'ch'开头

#字符串的转化
print(fruit.lower())#全部小写
print(fruit.upper())#全部大写
print('AbCd'.swapcase())#大小写互换
print(fruit.capitalize()) #首字母大写
print(fruit.title())#每个单词的首字母大写
print(fruit.encode(encoding='utf8')) #字符串转化成bytes类型
print(b'aaa'.decode(encoding='utf8'))#bytes类型转化成字符串

#字符串的格式化
print('my name is {name}'.format(name=fruit))#格式化
print('my name is {name}'.format_map({'name':fruit}))#格式化,可以使用字典带入
print('+'.join(['1','2','3']))#拼接字符使用
print('a b c d'.split(' '))#按照空格转化成列表默认空格
print('a\nb\n'.splitlines())#按照系统默认回车符号转化成列表,windws(\n),linux(\r\n)
print(' \npear'.lstrip())#去掉左边的全部空格和换行
print('pear \n'.rstrip())#去掉右边的全部空格和换行
print(' \npear \n'.strip())#去掉左右两边的全部空格和换行

#字符串的查找和替换
print(fruit.find('c'))#查找字母下标,不存在返回-1
print('abcda'.rfind('a'))#从右向左查找
print('abcda'.replace('a','1',2))#替换字母'a'需要替换的字母,'1'替换后的字母,2替换几次
p=str.maketrans('rry','***')#加密的方法
print(fruit.translate(p))#使用上方方法加密

#字符串的补齐
print(fruit.ljust(20,'-'))#总长度20,不足用'-'符号补齐,fruit左对齐
print(fruit.rjust(20,'-'))#总长度20,不足用'-'符号补齐,fruit右对齐
print(fruit.center(20,'-'))#总长度20,不足用'-'符号补齐,fruit居中
print(fruit.zfill(20))##总长度20,不足用0补齐

#字符串的统计
print(fruit.count('c')) #计算c在字符串中的个数