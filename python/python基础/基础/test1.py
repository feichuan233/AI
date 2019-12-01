#第一题 基于字典的通讯录
contact1={"phoneNum":"123","email":"不用（本人发言）","工作单位":"overwatch"}
contact2={"phoneNum":"456","email":"cowboy@gmail.com","工作单位":"overwatch"}
contact3={"phoneNum":"789","email":"OldLion@gmail.com","工作单位":"overwatch"}
contact={"hanzo":contact1,"mccree":contact2,"reinhardt":contact3}
#for k,v in contact.items():
#    print(k,v)

#创建一个把关键字转换为字典的函数
def turnToDict(**something):
    dict=something
    return dict

#创建一个遍历嵌套字典的函数



print("------Athena：欢迎来到ow通讯录，请问您需要我为您做些什么呢？------")
print("1.查询指定特工资料")
print("2.增加新的特工")
print("3.删除已有特工")
print("4.查询所有特工资料")
print("5.退出程序")
print("--------------------------------------------------------")

while True:
    try:
        choice=int(input())
        break
    except ValueError:
        print("Athena：无效选项，请您重新选择哦。")

#选项1 获取指定特工信息
if choice==1:
    while True:
        try:
            name=str(input("Athena：请输入特工名字"))
            break
        except ValueError:
            print("Athena：名字似乎不太对，再想想吧？")
    #在这一步后要通过名字获取
    #首先遍历外层字典获得名字和嵌套的字典
    for n,v in contact.items():
        #判断名字是否和输入的相等
        if n==name:
            #如果相等，则遍历该名字对应的嵌套循环，输出详细信息
            for k,v2 in v.items():
                print(k,v2)


#功能2 增加新特工
if choice==2:
    while True:
        strInput=str(input("Athena：请输入想加入的特工的姓名"))
        #判断输入的姓名是否已存在与通讯录内
        nameList=contact.keys()
        if strInput in nameList:
            print("Athena：已经有该特工了，不用再添加啦")
        else:
            break

    #输入新特工的三个必要参数，并通过创建字典的
    #函数将参数创建为字典
    numinput=str(input("Athena：请输入特工号码"))
    emaillInput=str(input("Athena：请输入特工emaill"))
    workplaceInput=str(input("Athena：请输入特工工作单位"))
    newDict=turnToDict(phoneNum=numinput,email=emaillInput,工作单位=workplaceInput)
    #最后将新的字典添加到通讯录中
    contact[strInput]=newDict
    #输出新的通讯录以检查是否成功添加
    for k1, v1 in contact.items():
        print("姓名：", k1)
        for k2, v3 in v1.items():
            print(k2, v3)

#功能3 删除指定特工信息
if choice==3:
    targetName=str(input("Athena：请输入想删除的特工姓名"))
    #以待删除特工名字为键删除内容
    contact.pop(targetName)
    print("Athena：删除完毕.")
    #输出删除后的通讯录以检查是否删除成功
    for k1, v1 in contact.items():
        print("姓名：", k1)
        for k2, v3 in v1.items():
            print(k2, v3)


#功能4 查询所有特工的信息
if choice==4:
    print("Athena：好的，即将为您展示目前所有特工的信息。")
    for k1,v1 in contact.items():
        print("姓名：",k1)
        for k2,v3 in v1.items():
            print(k2,v3)

if choice==5:
    print(input("Athena：明白了，请按下任意键退出吧。期待下次与您的会面"))


