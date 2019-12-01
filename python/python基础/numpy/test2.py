import numpy as np
import random as rd
#这里用了一个自定义的随机矩阵生成数组
def randonMatrix(sum,line,column):
    list1 = []
    num = 1
    while num <= sum:
        num2 = rd.randint(1, 100)
        list1.append(num2)
        num += 1
    a = np.asarray(list1).reshape(line, column)
    return a
a=randonMatrix(15,5,3)
b=randonMatrix(6,3,2)
print("第一个矩阵为")
print(a)
print("第二个矩阵为",b)
print("两个矩阵的矩阵积为：")
print(np.dot(a,b))#点积
print(np.matmul(a,b))#矩阵积