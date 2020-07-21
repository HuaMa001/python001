def getSum(scores):
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i]  # 累加
    return  sum
#計算平均方法
def getAvg(scores):
    sum =getSum(scores)
    avg=sum/len(scores)
    return  sum
#主程式
scores=[100, 93, 87, 75, 60]#數組
#print(scores[0])
#print(scores[1])
#print(scores[2])
#print(scores[3])
#print(scores[4])
print(len(scores))#數組的元素個數
#各科列印
for i in range(0, len(scores)):
    print(scores[i])
#求總分
sum=getSum(scores)
print("總分:%d" % sum)

#求平均?
avg = getAvg(scores)
print("平均:%1f"%avg)
