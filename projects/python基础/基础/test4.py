#第四题 创建一个10000行文件
import random
targetFile=open("D:\data.txt","w")
for i in range(10001):
    num=str(random.randint(1,100))
    num=num+"\n"
    targetFile.write(num)
targetFile.close()
print("执行完毕")