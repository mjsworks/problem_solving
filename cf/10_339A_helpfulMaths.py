# 339A_HelpfulMaths
# Solution

numbers = list(map(int, input().split("+")))

numbers.sort()

print("+".join(str(number) for number in numbers))