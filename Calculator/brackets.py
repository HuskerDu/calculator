import rpolish

def validate(e):
    flag=0
    for i in e:
        if i == '(':
            flag+= 1
        elif i== ')':
            flag-= 1
        if flag<0:
            return 0
    return 0 if flag!=0 else 1

def simplify(e):
    while '(' in e or ')' in e:
        for i in range(len(e)):
            if e[i] == '(':
                a=i
            elif e[i] == ')':
                b=i
                break
        m = rpolish.infix_to_post(e[a+1:b])
        n = rpolish.postfix_solve(m)
        e = '{}{}{}'.format(e[:a],str(n),e[b+1:])
    return e
