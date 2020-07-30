import statistics
import random

scores = []
for i in range(0, 10):
    scores.append(random.randint(0, 10))

def getStat(list):
    list.sort()
    mean = statistics.mean(scores)
    stdev = statistics.stdev(scores)
    cv = stdev / mean
    return mean, stdev, cv

a,b=[],[]
for i in range(0, 10):
    a.append(random.randint(0,10))
    b.append(random.randint(0,10))

print(a)
print(b)
mean_a, stedv_a, cv_a=getStat(a)
mean_b, stedv_b, cv_b=getStat(b)
print(mean_a, stedv_a, cv_a)
print(mean_b, stedv_b, cv_b)


















