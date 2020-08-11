class Account:
    __money=0 #(私人)物件屬性/變數 / 資產


    def __init__(self, x) -> None:
        self.__money = x #開戶時存的第一筆金額


    def transfer(self, accountName, x):
        print('轉帳給' + accountName + '金額:$'+ str(x))
        if x <= 0:
            print('轉帳金額必須大於0')
            return
        if x > self.__money:
            print('轉帳過大,餘額不足')
            return
        self.__money = self.__money - x


    def save(self,x):
        print('存款:$'+ str(x))
        if x <= 0:
            print('提款金額必須大於0')
            return
        self.__money = self.__money + x


    def withdraw(self,x): #x表示要提款金額
        print('提款:$'+str(x))
        if x <=0:
            print('提款金額必須大於0')
            return

        if x > self.__money:
            print('提款金額過大,餘額不足')
            return
        self.__money = self.__money - x


    def __str__(self) -> str:   #__str__ 印出
        return '帳戶餘額'+str(self.__money)



if __name__ == '__main__':
    account1= Account(30000)  #建立一個物件
    account1.money=9999 #__money私有屬性  不可更改
    print(account1)
    account1.withdraw(6000)
    print(account1)
    account1.save(1000)
    print(account1)
    account1.transfer('Mary',10000)
    print(account1)












