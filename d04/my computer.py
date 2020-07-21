def add(x, y):
    print("執行到 add() 方法", x, y)
    result=x+y
    return  result

#訊息說明方法
def info():
    print("執行到 info () 方法")
    print("本程式由 python 所撰寫")
    #return (可加可不加)

# 判斷性別
#A123456789
def checkSex(id):
    sex = id(1)
    if sex == "1":
        print("男性")
        return
    if sex == "2":
        print("女性")
        return





#主程式
sum=add(10, 20)
print(sum)
