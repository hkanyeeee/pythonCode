def deco(funcName):
    print("进行了一些操作")
    def func(a, b):
        print("还可以进行一些操作")
        funcName(a, b)
    return func

@deco
def func(a, b):
    print("输入了%d和%d"%(a,b))

func(10, 20)