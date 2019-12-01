import  numpy as np
import sys
a=np.array([[3,3.2],[3.5,3.6]])
b=np.array([[118.4],[135.2]])
a_inv=np.linalg.inv(a)
c=np.dot(a_inv,b)
print(c)
