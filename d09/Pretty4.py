def usd(func):
    def ineer(money):
        money=money/30
        return func(money)
    return ineer

def jpy(func):
    def ineer(money):
        money=money/0.28
        return func(money)
    return ineer


@usd
def exchange(money):
    print(money)

if __name__ == '__main__':
    exchange(10000)



