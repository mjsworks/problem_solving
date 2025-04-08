price, has, wants = map(int, input().split())
res = (wants*(wants+1)//2)*price-has
print("0" if res<0 else res)

'''
in the loop I would multiply payfor with increasing i. starting from 1 to n
so i replaced that with n*(n+1)/2 - i did floor division and that avoided the loop.
'''