class Caculate():
    def resolveEquation(self,line1,line2,line3,line4,value1,value2):
        import numpy as np
        a = np.array([[line1, line2], [line3, line4]])
        a_inv = np.linalg.inv(a)
        b = np.array([[value1], [value2]])
        print(a, b)
        result = np.dot(a_inv, b)
        print(result)