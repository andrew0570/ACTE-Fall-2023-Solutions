n,k=[int(x) for x in input().split()]
v=0
for i in range(n):
    s=input().split()
    if s[0]=='sphere':
        v+=3.14*int(s[1])**3*4/3
    elif s[0]=='cube':
        v+=int(s[1])**3
    elif s[0]=='cylinder':
        v+=3.14*int(s[1])**2*int(s[2])
    else:
        v+=3.14*int(s[1])**2*int(s[2])/3
print(int(v//k))