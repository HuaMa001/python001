exchange={
       'Usd': lambda money: print(money/30),
       'Jpy': lambda money: print(money*4)
}

exchange.get('Usd')(900)
exchange.get('Jpy')(900)
