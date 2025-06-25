# 318A_even odds
# Solution

# take inputs
n, k = map(int, input().split())

# breaking point
breaking_point = (n+1)//2

# odd number
if k<=breaking_point:
    print(2*k-1)
# even number
else:
    print(2*(k-breaking_point))
