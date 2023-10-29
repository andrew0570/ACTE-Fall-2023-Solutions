n=int(input())
for i in range(n):
    obj,sub=[x for x in input().split(",")]
    sub=sub.split()
    ver=sub[1:len(sub)]
    sub=list(sub[0])

    sub[0]=sub[0].upper()
    sub="".join(sub)
    obj=list(obj)
    obj[0]=obj[0].lower()
    obj="".join(obj)
    ver[-1]=list(ver[-1])
    ver[-1][-1]=' '
    ver[-1]="".join(ver[-1])
    ver=" ".join(ver)

    print(sub,ver+obj+".")