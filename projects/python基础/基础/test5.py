#第五题 读取第四题的文件，将数据存放到列表中，并打印行数和数据
targetFile=open("D:\data.txt","r")
dataList=[]
for i in targetFile:
    dataList.append(i)

for index,value in enumerate(dataList):
    print("第",index,"行:",value)