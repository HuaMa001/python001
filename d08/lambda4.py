if __name__ == '__main__':
    lev=['E','E','E','E','E','E','D','C','B','A','A',]
       #  0   1   2   3   4   5   6   7   8   9   10
    dict={
        'Level': lambda score : print(lev[score//10])
    }
    dict.get('Level')(95) #得到A
    dict.get('Level')(85) #得到B
    dict.get('Level')(75) #得到C
    dict.get('Level')(65) #得到D
    dict.get('Level')(55) #得到E
    dict.get('Level')(25) #得到E






