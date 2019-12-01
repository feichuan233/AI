def randonMatrix(sum,line,column):
    "用于生成随机矩阵的函数，三个参数分别是总元素数，行数，列数"
    import random as rd
    import numpy as np
    list1 = []
    num = 1
    while num <= sum:
        num2 = rd.randint(1, 100)
        list1.append(num2)
        num += 1
    print(len(list1))

    a = np.asarray(list1).reshape(line, column)
    return a

