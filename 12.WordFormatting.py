n,k=[int(x) for x in input().split()]
line=input()
line=line.split(" ")
i=0
while i<len(line):
    l=0
    while i<len(line) and l+len(line[i])<=k:
        print(line[i],end=' ')
        l+=len(line[i])
        i+=1
    print("")
        