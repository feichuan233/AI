import random as rd
import numpy as np
#调用自定义随机矩阵生产函数
def randonMatrix(sum,line,column):
    list1 = []
    num = 1
    while num <= sum:
        num2 = rd.randint(1, 100)
        list1.append(num2)
        num += 1
    a = np.asarray(list1).reshape(line, column)
    return a

a=randonMatrix(6,1,6)
list2=[2,41,5,6,513]
# print("冒泡排序前：",a)
# a.sort()
# print("冒泡排序后",a)

for i in range(len(list2)-1):
    for j in range(len(list2)-1-i):
        if list2[j]>list2[j+1]:
            a=list2[j]
            b=list2[j+1]
            list2[j]=b
            list2[j + 1]=a


print(list2)
