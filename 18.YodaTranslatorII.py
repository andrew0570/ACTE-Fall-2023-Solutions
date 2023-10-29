k=int(input())
for l in range(k):
    n=input().split()
    i=0
    n[0]=n[0].lower()
    while not ',' in n[i]:i+=1
    n[i]=n[i][:-1]
    n[-1]=n[-1][:-1]
    n.reverse()
    n[0]=n[0].capitalize()
    n[i]=n[i]+','
    n[-1]=n[-1]+'.'
    print(" ".join(n))