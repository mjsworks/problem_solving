# 231A_Team
# Solution
num_input = int(input())
count = 0
for i in range(num_input):
    # 3 integer definition would be the simplest and fastest
    a, b, c = map(int, input().split()) # apply the function to each of the variable
    count+=1 if (a+b+c) >= 2 else 0

print(count)