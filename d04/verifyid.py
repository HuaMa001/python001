def areaNum(area):
    if area =='A':
        return '10'
    elif area =='F':
        return '15'
    elif area == 'H':
        return '17'
    elif area == 'M':
        return '21'
    elif area == 'B':
        return '11'
    elif area == 'C':
        return '12'
    elif area == 'D':
        return '13'
    elif area == 'E':
        return '14'
    elif area == 'G':
        return '16'
    elif area == 'I':
        return '34'
    elif area == 'J':
        return '18'
    elif area == 'K':
        return '19'
    elif area == 'N':
        return '21'
    elif area == 'O':
        return '22'
    elif area == 'P':
        return '23'
    elif area == 'Q':
        return '24'
    elif area == 'T':
        return '27'
    elif area == 'U':
        return '28'
    elif area == 'V':
        return '29'
    elif area == 'W':
        return '32'
    elif area == 'X':
        return '30'
    elif area == 'Z':
        return '33'

def verifyId(id):
    id2 = areaNum(id[0]) + id[1] + id[2] + id[3] + id[4] + id[5] + id[6] + id[7] + id[8] + id[9]
    delta = '19876543211'
    print(id)
    print(id2)
    print(delta)
    sum = int(id2[0]) * int(delta[0]) + \
          int(id2[1]) * int(delta[1]) + \
          int(id2[2]) * int(delta[2]) + \
          int(id2[3]) * int(delta[3]) + \
          int(id2[4]) * int(delta[4]) + \
          int(id2[5]) * int(delta[5]) + \
          int(id2[6]) * int(delta[6]) + \
          int(id2[7]) * int(delta[7]) + \
          int(id2[8]) * int(delta[8]) + \
          int(id2[9]) * int(delta[9]) + \
          int(id2[10]) * int(delta[10])
    print(sum)
    print("正確" if sum % 10 == 0 else "錯誤")

# 主程式
id = input('請輸入身份證字號: ')
verifyId(id)





