'''
thought process:
instead of going for a brute-force approach, we can just divide the number by 5. id it is divisible, great.
else, it is going to take any step from 1-4, which counts as 1.
so, if we just divide with 5 and there is a remainder, we can just increase the count with 1
else, the count is the division value.
'''

num = int(input())
print(num//5 if num%5==0 else (num//5)+1)