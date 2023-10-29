n=int(input())
total=0
a=0
b=0
c=0
d=0
f=0
for i in range(n):
    g,p=input().split()
    total+=int(p)
    if g=='A':a+=1
    elif g=='B':b+=1
    elif g=='C':c+=1
    elif g=='D':d+=1
    else: f+=1
print(a)
print(b)
print(c)
print(d)
print(f)
print(round(total/n, 2))