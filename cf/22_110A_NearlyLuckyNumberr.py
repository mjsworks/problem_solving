num = input()
count = 0
for i in range(len(num)):
    if num[i]=='4' or num[i]=='7':
        count+=1

flag=0
for ch in str(count):
    if ch!='4' and ch!='7':
        flag=0
        break
    else:
        flag=1
print("YES" if flag==1 else "NO")