# 158A_NextRound
# Solution

n,k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
cutoff = a[k-1]
for score in a:
    count+=1 if score>=cutoff and score>0 else 0
    
print(count)