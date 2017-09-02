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
