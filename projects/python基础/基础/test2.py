#第二题 计算圆的周长和面积 球体的表面积和体积
class CaculateClass():
    #计算用的类
    def caculateCircular(self,radius):
        areaValue = 3.14 * radius * radius
        circumference = 2 * radius * 3.14
        print("圆的周长为:", circumference, "圆的面积为：", areaValue)

    def caculateSphere(self,radius):
        areaValue = 4 * 3.14 * radius * radius
        volume = (4 / 3) * 3.14 * (radius ** 3)
        print("球体的表面积为：", areaValue, "球体的体积为", volume)

a=CaculateClass()
a.caculateCircular(20)
a.caculateSphere(20)