# 263A_BeautifulMatrix
# Solution

# word1, word2 = map(str, input().split())
word1 = input().lower()
word2 = input().lower()

res = 1 if word1>word2 else -1 if word1<word2 else 0
print(res)

'''
map(function, iterable)
map basically applied the functions to every item in iterable
map(str, ***) - is redundant as the inputs are str by nature. so str does nothing here.
input().split() will also return a list.
'''