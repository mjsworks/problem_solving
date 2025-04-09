word = input()
upper, lower = 0, 0
for char in word:
    if char.isupper():
        upper+=1
    else char.islower():
        lower+=1

flag = 1 if upper>lower else 0
print(word.upper() if flag==1 else word.lower())
