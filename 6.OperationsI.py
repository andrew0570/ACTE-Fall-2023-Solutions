n=int(input())
for i in range(n):
    f1,o,f2,e,s=[x for x in input().split()]
    f1=int(f1)
    s=int(s)
    if o=='+':print(s-f1)
    elif o=='-':print(f1-s)
    elif o=='*':print(int(s/f1))
    else:print(round(f1/s))