#coding=utf-8
#Author:gm
import os,sys
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
choice_list=['账户信息','取款','还款','退出']
from core import views
choice_dic={
    '账户信息':views.user_info,
    '取款':views.draw_money,
    '还款':views.save_money,
    '退出':exit
}
@views.verify
def run():
    print('welcome to the main page')
    while True:
        for index,value in enumerate(choice_list):
            print(index+1,value)
        choice=input('===>选择:').strip()
        choice=int(choice)
        choice_key=choice_list[choice-1]
        print(choice_key)
        choice_dic[choice_key]()






