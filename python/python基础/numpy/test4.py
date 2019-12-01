#获取一维数组中0元素的索引位置
import numpy as np
a=np.array([1,2,0,0,4])
num=0
#用for的形式来输出0的索引位置
for i in a:
    if i==0:
        print(num)
    num+=1

#where函数会返回元组，以元组的形式输出0的索引位置
tuple1=np.where(a==0)
print(tuple1)

