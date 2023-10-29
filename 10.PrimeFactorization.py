n=[int(input())]

loop=True
while loop:
    loop=False
    for i in range(2,n[-1]+1):
        if i==n[-1]:break
        if n[-1]%i==0:
            n.insert(-1, i)
            n[-1]=int(n[-1]/i)
            loop=True
            break
for i in n:
    print(i, end=' ')
print()