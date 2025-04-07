# 266A_Stones on a table
# Solution

num = int(input())
word = input()
count = 0
for i in range(1,num):
    if word[i]==word[i-1]:
        count+=1

print(count)