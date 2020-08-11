# 特過裝飾器檢核參數
def confirm(func):
    def ineer(a, b):
        if b == 0:
            print('分母不可為0')
            return 0
        return func(a, b)
    return ineer

@confirm
def div(a,b):
    return a/ b

if __name__ == '__main__':
    print(div(10, 2))
    print(div(10, 0))


