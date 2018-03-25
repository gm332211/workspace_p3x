#coding=utf-8
#Author:gm
import xml.etree.ElementTree as ET
tree=ET.parse('test.xml')
#tag获取标签名称,attrib获取属性名称和值,text获取标签内容
print(tree.getroot())
for country in tree.getroot():
    print(country.tag,country.attrib,country.text)
    for pro in country:
        print(pro.tag,pro.attrib,pro.text)
#修改
root=tree.getroot()
for year in root.iter('year'):
    new_year=int(year.text)-1
    year.text=str(new_year)#修改内容
    year.set('update','yes')#增加一个属性
tree.write('test.xml')#在次写入
#删除
for country in root.findall('country'):
    rank=int(country.find('rank').text)
    if rank>50:
        root.remove(country)
tree.write('test.xml')
#创建一个新的xml文件
new_xml=ET.Element('namelist')#创建跟
prosen=ET.SubElement(new_xml,'prosen',attrib={'enabled':'true'})#创建主分支
name=ET.SubElement(prosen,'name',attrib={'enabled':'true'})#创建副分支
age=ET.SubElement(prosen,'age',attrib={'enabled':'true'})
name.text='xiaoming'
age.text='22'
et=ET.ElementTree(new_xml)#生成对象
et.write('test2.xml',encoding='utf-8',xml_declaration=True)#生成文件
ET.dump(new_xml)#打印格式