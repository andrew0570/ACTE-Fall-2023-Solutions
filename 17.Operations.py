e=input()
if '+' in e:
    a,b=e.split('+')
    print(str(int(a)+int(b)))
elif '-' in e:  
    a,b=e.split('-')
    print(str(int(a)-int(b)))
elif '*' in e:
    a,b=e.split('*')
    print(str(int(a)*int(b)))
    
else:
    a,b=e.split('/')
    print(str(round(int(a)/int(b))))