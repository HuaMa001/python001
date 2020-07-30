import random

def getScores(p):
    if p =="A":
        return 1
    elif p =="J" or p =="Q" or p == "K":
        return 0.5
    return p #2-10數字
poker=["A",2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,"J" ,"Q" ,"K"]*4
random.shuffle(poker)#洗牌
#print("牌",poker)
#牌局開始 先發1張
p1=poker.pop()
sum=getScores(p1)
print("已拿",p1,"總分",sum)
#print("剩餘",poker)
#繼續拿牌?
count_user=0;
while True:
    ask=input("是否繼續拿牌?(y/n)")
    if ask =="y":
        p = poker.pop()
        sum+=getScores(p)
        print("再拿",p,"總分",sum)
        if sum>10.5:
            print("user爆了")
            break
        else:
            count_user+=1
        if count_user ==5:
            print("user過五關")
            break

    else:
        break












