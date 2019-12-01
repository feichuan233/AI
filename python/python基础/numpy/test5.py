#创建一个随机10*10矩阵，并求最大值和最小值
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
a=randonMatrix(100,10,10)
print(a)

print(np.max(a))
print(np.min(a))