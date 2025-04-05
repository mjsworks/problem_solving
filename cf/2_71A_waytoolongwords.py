# 71_a_way too long words
num_inputs = int(input())

for i in range (num_inputs):
    word = str(input())
    if len(word)>10:
        print(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        print(word)