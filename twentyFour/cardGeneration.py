from random import randint

def generate24():
    res3 = 0
    while(res3 != 24):
        op1 = randint(0, 3)
        op2 = randint(0, 3)
        op3 = randint(0, 3)

        res1 = 0
        res2 = 0
        res3 = 0
        res4 = 0

        num1 = float(randint(1, 10))
        num2 = float(randint(1, 10))
        num3 = float(randint(1, 10))
        num4 = float(randint(1, 10))

        resarray = []

        if (op1 == 0):
            res1 = num1 + num2
        elif (op1 == 1):
            res1 = num1 - num2
        elif (op1 == 2):
            res1 = num1 * num2
        elif (op1 == 3):
            res1 = num1 / num2

        if (op2 == 0):
            res2 = res1 + num3
        elif (op1 == 1):
            res2 = res1 - num3
        elif (op1 == 2):
            res2 = res1 * num3
        elif (op1 == 3):
            res2 = res1 / num3

        if (op3 == 0):
            res3 = res2 + num4
        elif (op3 == 1):
            res3 = res2 - num4
        elif (op3 == 2):
            res3 = res2 * num4
        elif (op3 == 3):
            res3 = res2 / num4


    resarray.append(int(num1))
    resarray.append(int(num2))
    resarray.append(int(num3))
    resarray.append(int(num4))
    return resarray

def generateSet():
    return generate24()

# print generateSet()