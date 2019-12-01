#创建一个长度为10的一维全为0的ndarray对象，然后让第五个元素等于1
import numpy as np
a=np.zeros(10,dtype=int)
a[5:6:1]=5
print(a)