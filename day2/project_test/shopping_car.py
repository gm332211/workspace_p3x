#coding=utf-8
#Author:gm
#readme:运行程序输入金额,进入商品列表,选择数字购买,按q退出
commodity=[['apple','5'],['cherry','2'],['banana','1'],['grape','1']]
shopping_car=[]
#金额的输入
while True:
    cash=input('你需要多少钱:')
    if cash.isdigit():
        break
    else:
        print('请输入正整数!')
cash=int(cash)
flag=True
while cash>=0:
    #main
    #打印商品列表
    for i in range(len(commodity)):
        print('%s. %s 价格$%s'%(i+1,commodity[i][0],commodity[i][1]))
    print('你的金额:$%s'%(cash))
    commodity_id=input('购买:')
    #停止购买的条件
    if commodity_id=='q':
        break
    if commodity_id.isdigit():
        commodity_id = int(commodity_id)
    else:
        print('请输入正整数!')
        continue
    if commodity_id > len(commodity) or commodity_id < 1:
        print('没有件商品')
        continue
    comm_index = commodity_id-1
    #主要的逻辑判断
    if int(commodity[comm_index][1]) <= cash:
        shopping_car.append(commodity[comm_index])
        cash = cash - int(commodity[comm_index][1])
        print('成功购买%s'%(commodity[comm_index][0]))
    else:
        print('对不起你的金额不足')
print('------你的购物车------')
for i in shopping_car:
    print(i)
print('你的余额$%s'%(cash))
