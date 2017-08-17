from operator import add, sub, mul, truediv


####################################################
#Converting from infix notation to postfix notation#
####################################################

def infix_to_post(s):
    try:
        stack, b = [], []
        a = s.split()
        for i in a:
            if i not in '/*-+':
                b.append(i)
            else:
                if not stack:
                    stack.append(i)
                else:
                    if stack[-1] in '+-' and i in '*/':
                        stack.append(i)
                    else:
                        while stack:
                            b.append(stack.pop())
                        stack.append(i)
        while stack:
            b.append(stack.pop())
        return ' '.join(b)
    except:
        return 0


##########################
#Solving postfix notation#
##########################

def postfix_solve(s):
    try:
        op = {'+': add, '-': sub, '*': mul, '/': truediv}
        stack = []
        c = s.split()
        for i in c:
            if i in op:
                a, b = stack.pop(), stack.pop()
                stack.append(op[i](float(b), float(a)))
            elif i:
                stack.append(i)
        return stack.pop()
    except:
        return 0 
