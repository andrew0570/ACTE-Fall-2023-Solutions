a,b=[int(x) for x in input().split()]
x,y=[int(x) for x in input().split()]
count1=abs(b-a)
if abs(x-a)+1+abs(y-b)>abs(y-a)+1+abs(x-b):
    count2=abs(y-a)+1+abs(x-b)
else:
    count2=abs(x-a)+1+abs(y-b)
print(min(count1,count2))