n=int(input())
for i in range(n):
    num,x,z=[int(x) for x in input().split()]
    if z<x: x,z=z,x

    if num%2==0 and z-x==num/2: print(0)
    else:
        count=min(z-x-1,num-z+x-1)
        a=count
        while a<num-a-2:
            a+=1

        print(count+(a-count)*2-2)