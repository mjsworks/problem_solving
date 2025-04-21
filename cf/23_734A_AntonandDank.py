num = int(input())
inp = input()
anton, danik = 0, 0
for ch in inp:
    if ch=="A":
        anton+=1
    else:
        danik+=1

print("Anton" if anton > danik else "Danik" if danik > anton else "Friendship")