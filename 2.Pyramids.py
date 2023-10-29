n=int(input())
for i in range(n):
    for k in range(n-i-1):
        print("  ", end='')
    for k in range(2*i+1):
        if k==2*i:print("X", end='')
        else: print("X ", end='')
    print()