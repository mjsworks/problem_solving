# 236A_boy or girl
# Solution

inp = input()

res = "CHAT WITH HER!" if len(set(inp))%2==0 else "IGNORE HIM!"

print(res)