n=input().split()

for i in range(len(n)):
    l=len(n[i])
    for k in n[i]:
        if k.isalpha()==False:
            l-=1
    l/=2
    if type(l) is float:
        l+=.5
        l=int(l)
    a=0
    n[i]=list(n[i])
    for k in range(l):
        while n[i][a].isalpha()==False:
            a+=1
        n[i][a]=n[i][a].upper()
        a+=1
    n[i]="".join(n[i])
n=" ".join(n)
print(n)