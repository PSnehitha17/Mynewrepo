s=input().lower
r=''
for p in range(97,123):
    d=chr(p)
    if d not in s:
        r=r+d
print(r) if(len(r)>0) else print("0")
