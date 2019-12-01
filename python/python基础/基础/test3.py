#第三题 华氏度和摄氏度转换
class temperature():
    #计算温度用的类
    def centigradeToFahrenheit(self,centi):
        "摄氏度转华氏度"
        fahrenheit=int(9*centi/5+32)
        return fahrenheit

    def fahrenheitTocentigrade(self,fahren):
        "华氏度转摄氏度"
        centigrade=int(5*(fahren-32)/9)
        return centigrade

test=temperature()
#测试摄氏度转华氏度
print("当前摄氏度的华氏度为：",test.centigradeToFahrenheit(20))
#测试华氏度转摄氏度
print("当前华氏度的摄氏度为：",test.fahrenheitTocentigrade(20))