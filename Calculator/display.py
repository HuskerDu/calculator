#This file is used for displaying input/output of the equation in the calculator

import rpolish

class Display:

    equation = ''

    def get_eqn(self, s, eqn):
        try:
            if s == 'Del':
                if self.equation!= '':
                    self.equation = list(self.equation)
                    del(self.equation[-1])
                    self.equation = ''.join(self.equation)
                    eqn.set(self.equation)
            elif s == 'AC':
                self.equation = ''
                eqn.set(self.equation)
            elif s == '=':
                reverse_polish = rpolish.infix_to_post(self.equation)
                ok = rpolish.postfix_solve(reverse_polish)
                self.equation = ''
                if ok is 'No':
                    raise ValueError
                eqn.set(ok)
            elif s in '+-/*':
                if len(self.equation) == 0 or len(self.equation) > 2 and self.equation[-2] in '+-*/':
                    if s in '-+':
                        self.equation +=s
                else:
                    self.equation += " {} ".format(s)
                eqn.set(self.equation)
            else:
                self.equation += s
                eqn.set(self.equation)
        except:
            eqn.set('Error')
