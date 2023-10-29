n=int(input())
for i in range(n):
    e=input()
    e=list(e)
    e.pop()

    #combine numbers
    for k in range(len(e)):
        if e[k].isdigit(): e[k]=int(e[k])
    k=0
    while True:
        a=e[k]
        b=e[k+1]
        if type(a) is int and type(b) is int:
            e[k]=a*10+b
            e.pop(k+1)
        else: k+=1
        if k>=len(e)-1: break
        
    #solve parenthises by breaking down equation into left and right bounds of list   
    while '(' in e:
        left=e.index('(')
        right=e.index(')')
        while '(' in e[left+1:right]:
            left=e[left+1:right].index('(')
        
        while '^' in e[left:right]:
            a=min(loc for loc,x in enumerate(e[left:right]) if x=='^')+left
            e[a-1]=e[a-1]**e[a+1]
            e.pop(a+1)
            e.pop(a)
            right-=2
        while '*' in e[left:right] or '/' in e[left:right]:
            a=min(loc for loc,x in enumerate(e[left:right]) if x=='*' or x=='/')+left
            if e[a]=='*':
                e[a-1]=e[a-1]*e[a+1]
            else:
                e[a-1]=e[a-1]/e[a+1]
            e.pop(a+1)
            e.pop(a)
            right-=2
        while '+' in e[left:right] or '-' in e[left:right]:
            a=min(loc for loc,x in enumerate(e[left:right]) if x=='+' or x=='-')+left
            if e[a]=='+':
                e[a-1]=e[a-1]+e[a+1]
            else:
                e[a-1]=e[a-1]-e[a+1]
            e.pop(a+1)
            e.pop(a)
            right-=2
        e.pop(left)
        e.pop(right-1)

    while '^' in e:
        a=min(loc for loc,x in enumerate(e) if x=='^')
        e[a-1]=e[a-1]**e[a+1]
        e.pop(a+1)
        e.pop(a)

    k=0
    if len(e)>=2:
        while True:
            a=e[k]
            b=e[k+1]
            if type(a) is int and type(b) is int:
                e[k]=a*b
                e.pop(k+1)
            else: k+=1
            if k>=len(e)-1: break

    #solve the rest
    while '*' in e or '/' in e:
        a=min(loc for loc,x in enumerate(e) if x=='*' or x=='/')
        if e[a]=='*':
            e[a-1]=e[a-1]*e[a+1]
        elif e[a]=='/':
            e[a-1]=e[a-1]/e[a+1]
        e.pop(a+1)
        e.pop(a)
    while '+' in e or '-' in e:
        a=min(loc for loc,x in enumerate(e) if x=='+' or x=='-')
        if e[a]=='+':
            e[a-1]=e[a-1]+e[a+1]
        elif e[a]=='-':
            e[a-1]=e[a-1]-e[a+1]
        e.pop(a+1)
        e.pop(a)
    print(e[0])