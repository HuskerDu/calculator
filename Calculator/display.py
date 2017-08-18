import rpolish

equation=''

def get_eqn(s, eqn):
    global equation
    try:
        if s == 'Del':
            if equation!= '':
                equation = list(equation)
                del(equation[-1])
                equation = ''.join(equation)
                eqn.set(equation)
        elif s == '=':
            reverse_polish = rpolish.infix_to_post(equation)
            ok = rpolish.postfix_solve(reverse_polish)
            equation = ''
            if ok is 'No':
                raise ValueError
            eqn.set(ok)
        elif s in '+-/*':
            if len(equation) == 0 or len(equation) > 2 and equation[-2] in '+-*/':
                if s in '-+':
                    equation +=s
            else:
                equation += " {} ".format(s)
            eqn.set(equation)
        else:
            equation += s
            eqn.set(equation)
    except:
        eqn.set('Error')
