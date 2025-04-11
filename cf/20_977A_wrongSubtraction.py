n, k = map(int, input().split())
for i in range(0, k):
    n = n-1 if n%10!=0 else n//10

print(n)