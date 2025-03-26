# 282A_Bit++
# Solution

n = int(input())
res = 0
for i in range(n):
    inp = input()
    res+=1 if "+" in inp else -1
    
print(res)