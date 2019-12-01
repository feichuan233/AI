#提示输入两个数
while True:
    try:
        a=int(input("请输入第一个数字"))
        b=int(input("请输入第二个数字"))
        break
    except ValueError:
        print("输入的类型不对哦！")
print(a+b)