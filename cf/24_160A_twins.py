inp = int(input())
coins = list(map(int,input().split()))
coins.sort(reverse=True)
half = sum(coins)//2

myOne, mySum=0,0
for coin in coins:
    if half>=mySum:
        mySum+=coin
        myOne+=1
    else:
        break

print(myOne)