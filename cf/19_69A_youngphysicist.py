n = int(input())
sumx, sumy, sumz = 0, 0, 0
for i in range(0,n):
    x, y, z = map(int, input().split(" "))
    sumx = sumx+x
    sumy = sumy+y
    sumz = sumz+z

print("YES" if sumx==0 and sumy==0 and sumz==0 else "NO")