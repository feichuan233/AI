import numpy as np
from PIL import  Image
from matplotlib import  pyplot as plt
# from scipy.misc
"第七天上机题:"
"第一题"
# a=np.array([[7,2],[3,4],[5,3]])
# U,V,D=np.linalg.svd(a)
# print("U:")
# print(U)
# print("V:")
# print(V)
# print("D:")
# print(D)

"第二题"
"""思路：用Image的open方法获取一个对象，用convert指定色彩
然后用img对象的getdata方法获取数据，并将数据转换为列表，
再将列表用array方法转换为数组，再用reshape方法将这个数组转换为图片的大小
"""
# #设置循环以依次显示sv个数为5，10，20，30时的图像
# img=Image.open("C:\\Users\\Lenovo\\Desktop\\QQ图片20191018102440.jpg")
# #print(img)
# imggray=img.convert("LA")
# #
# imgmat=np.array(list(imggray.getdata(band=0)),float)
# newimg=imgmat.reshape(412,621)
# U,D,V=np.linalg.svd(newimg)
# for i in [5,10,20,30]:
#
#     #img = Image.open("C:\\Users\\Lenovo\\Desktop\\QQ图片20191018102440.jpg")
#     #旁听到的知识，👇被划线的方法是不推荐使用的方法
#     reconsting=np.matrix(U[:,:i])*np.diag(D[:i])*np.matrix(V[:i,:])
#     plt.imshow(reconsting,cmap="gray")
#     title="n=%s"%i
#     plt.title(title)
#     plt.show()


"第三题"
np.random.seed(123)
x=5*np.random.rand(100)
y=2*x+1+np.random.randn(100)
x=x.reshape(100,1)
y=y.reshape(100,1)
A=np.hstack((x,np.ones(np.shape(x))))
A[:10]
print(A)
A_plus=np.linalg.pinv(A)
conefs=A_plus.dot(y)
print(conefs)
x_line=np.linspace(0,5,1000)
y_line=conefs[0]*x_line+conefs[1]
plt.plot(x,y,"*")
plt.plot(x_line,y_line)
plt.show()