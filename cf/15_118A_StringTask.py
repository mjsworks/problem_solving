# 118A_String task
# Solution

alphs = input().lower()

print(''.join('.'+alph for alph in alphs if alph not in ('aeiouy')))