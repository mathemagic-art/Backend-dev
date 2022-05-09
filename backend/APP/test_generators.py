from operator import ge
from pydoc import apropos
from random import choice, randint, choices
from regex import E
from scipy import rand
from sympy import Symbol, sympify, Symbol, oo, Integer, latex, expand, simplify, trigsimp
from re import search
from latex2sympy2 import latex2sympy


x = Symbol('x')

#################################################################################
# functions generators

def linear_func(coeff=randint(1, 5), free=randint(0, 10)):
    problem = "{}*x+{}".format(coeff, free)
    return problem

def polynomial(coeff=randint(-5, 5), power=randint(0, 5), number_of_members = randint(1, 4)):
    problem = ''
    problem += "{}*x**{}".format(coeff, power)
    for i in range(number_of_members):
        coeff = randint(-5, 5)
        power = randint(0, 5)
        problem += "+{}*x**{}".format(coeff, power)
    return problem

def trigonometric(level=0):
    list_of_func = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc']
    problem = choice(list_of_func)
    if level == 0:
        problem += '(x)'
    elif level == 1:
        problem += '({})'.format(linear_func())
    else:
        problem += '({})'.format(polynomial())
    return problem

def arcfunc(level=0):
    list_of_func = ['asin', 'acos', 'atan', 'acot', 'sec', 'csc']
    problem = choice(list_of_func)
    if level == 0:
        problem += '(x)'
    elif level == 1:
        problem += '({})'.format(linear_func())
    else:
        problem += '({})'.format(polynomial())
    return problem
    return problem

def expon(level=0, base = choices(['1', '2', 'E', '3', '4'], weights=[1, 1, 3, 1, 1], k = 1)[0]):
    if level == 0:
        problem = '{}**(x)'.format(base)
    elif level == 1:
        problem = '{}**({})'.format(base, linear_func())
    else:
        problem += '{}**({})'.format(base, polynomial())
    return problem

def lg(level=0, base = choices(['1', '2', 'E', '3', '4'], weights=[1, 1, 3, 1, 1], k = 1)[0]):
    if level == 0:
        problem = 'log(x, {})'.format(base)
    elif level == 1:
        problem = 'log({}, {})'.format(linear_func(),base)
    else:
        problem = 'log({}, {})'.format(polynomial(),base)
    return problem

######################################################################################
# latex output converter and input

def parse_func(function: str) -> str: 
    try:
        function = sympify(function.replace('e', 'E'), convert_xor=True)
    except:
        function = function.replace('\frac', '\\frac')
        function = function.replace('\tan', '\\tan')
        function = function.replace('\arcsin', '\\arcsin')
        function = function.replace('\arccos', '\\arccos')
        function = function.replace('\arctan', '\\arctan')
        function = function.replace('\arccot', '\\arccot')
        function = latex2sympy(function)
    return function


def output_func2(function: str): ## consider the case when we are multiplying function with log [sin(x)*log(x)]/[log(3)] or [x**2*log(x)]/[sin(x)*log(2)]
    function = latex(sympify(function))
    function = str(function).replace('log', 'ln')
 
    # copy_func = function                       unstabel working part
    # for i in ['\\', 'left', 'right', '(', ')', ' ']:
    #     copy_func = copy_func.replace(i, '')
    
    # while search('frac\{(.*?)ln\{(.*?)\}\}\{(.*?)ln\{(.*?)\}\}', copy_func) != None:
    #     expr = search('frac\{(.*?)ln\{(.*?)\}\}\{(.*?)ln\{(.*?)\}\}', copy_func).string
    #     ind_of_expr = list(search('frac\{(.*?)ln\{(.*?)\}\}\{(.*?)ln\{(.*?)\}\}', copy_func).span())
    #     print(expr)
    #     def get_key_ind(index, num, iter, expr):
    #         '''This function is for finding the boarder indexies of the expression '''
    #         ind = index + num
    #         key_ind = 0
    #         for i in range(iter):
    #             n = 0
    #             while True:
    #                 if expr[ind] == '{':
    #                     n += 1
                
    #                 elif expr[ind] == '}':
    #                     n -= 1
                        
    #                 if n == 0:
    #                     key_ind = ind
    #                     break
    #                 ind += 1
    #             ind = key_ind + 1
    #         return key_ind
    #     key_ind = get_key_ind(ind_of_expr[0], 5, 2, function)

    #     def edit_inner_func(expr):
    #         result = expr
    #         expr_copy = expr
    #         changed_expr = expr
    #         for i in ['ln', 'sin', 'cos', 'tan', 'cot', 'arcsin', 'arccos', 'arctan', 'arccot']:
    #             while i in expr_copy:
    #                 init_ind, end_ind = search('{}'.format(i)+'\{(.*?)\}', expr).span()
    #                 subexpr = '\\' + expr[init_ind:init_ind+len(i)+1] + '(' + expr[init_ind+len(i)+1: end_ind-1] + ')' + '}'
    #                 changed_expr = expr[:init_ind] + subexpr + expr[end_ind:]
    #                 expr_copy = expr[:init_ind] + expr[end_ind:] 
    #             result = changed_expr
    #         return result
    #     subexpr = search('(.*?)ln\{(.*?)\}', expr).string
    #     coeff_id = search('(.*?)ln\{(.*?)\}', expr).span()[0]
    #     coeff1 = ''
    #     while subexpr[coeff_id] != 'l':
    #         if subexpr[coeff_id] not in ['f', 'r', 'a', 'c', '{']:
    #             coeff1 += subexpr[coeff_id]
    #         coeff_id += 1
    #     print(coeff1)
    #     init_ind = search('ln\{(.*?)\}', expr).span()[0]
    #     end_ind = get_key_ind(0, 7+len(coeff1), 1, expr)
    #     log_expr = expr[init_ind+2:end_ind+1]
        
    #     expr = expr[end_ind+1:]
    #     subexpr = search('(.*?)ln\{(.*?)\}', expr).string
        
    #     coeff_id = search('(.*?)ln\{(.*?)\}', expr).span()[0]
    #     coeff2 = ''
    #     while subexpr[coeff_id] != 'l':
    #         if subexpr[coeff_id] not in ['{', '}']:
    #             coeff2 += subexpr[coeff_id]
    #         coeff_id += 1
    #     print(coeff2)
    #     init_ind = search('ln\{(.*?)\}', expr).span()[0]
    #     end_ind = get_key_ind(init_ind, 2, 1, expr)
    #     log_base = expr[init_ind+2:end_ind+1]
    #     if coeff1 == '':
    #         if coeff2 != '':
    #             function = function[:ind_of_expr[0]] + "\\frac{{1}}y{{{}}}\\log_{} ({})".format(coeff2, edit_inner_func(log_base), edit_inner_func(log_expr)) + function[key_ind+1:] 
    #         else:
    #             function = function[:ind_of_expr[0]] + "\\log_{} ({})".format(coeff2, edit_inner_func(log_base), edit_inner_func(log_expr)) + function[key_ind+1:] 
    #     elif coeff2 == '':
    #         if coeff1 != '':
    #             function = function[:ind_of_expr[0]] + "{}\\log_{} ({})".format(coeff1, edit_inner_func(log_base), edit_inner_func(log_expr)) + function[key_ind+1:] 
    #         else:
    #             function = function[:ind_of_expr[0]] + "\\log_{} ({})".format(coeff2, edit_inner_func(log_base), edit_inner_func(log_expr)) + function[key_ind+1:]
    #     else:
    #         function = function[:ind_of_expr[0]] + "\\frac{{{}}}{{{}}}\\log_{} ({})".format(coeff1, coeff2, edit_inner_func(log_base), edit_inner_func(log_expr)) + function[key_ind+1:] 
    #     copy_func = function
    return function


# test generators 

def generateDifferentiation(level='1'):

    # dependencies
    problem = ''
    # logic
    if level == '1':
        problem += polynomial()

    if level == '2':
        problem += polynomial() + '+{}*'.format(randint(-5, 5)) + trigonometric(1)

    if level == '3':
        problem += polynomial() + '+{}*'.format(randint(-5, 5)) + trigonometric(1) + '+{}*'.format(randint(-5, 5)) + expon(1) + '+{}*'.format(randint(-5, 5)) + lg(1)
    if level == '4':
        problem += '(' + polynomial() + '+{}*'.format(randint(-5, 5)) + trigonometric(1) + '+{}*'.format(randint(-5, 5)) + expon(1) + '+{}*'.format(randint(-5, 5)) + lg(3) + '+' + arcfunc(0) +')/(' + polynomial() + ')'

    problem = sympify(str(sympify(problem)).replace('zoo', '5'))
    print(problem)
    problem = output_func2(problem)
    return problem


def generateLimit(level='1'):
    problem = ''
    if level == '1': #добавить, чтобы лимит был равен какому ненулевовму значению с choices

        problem += '(' + polynomial() + ')/(' + polynomial() + ')'
        approach = oo

    if level == '2':
        coeff = randint(1, 5)
        free = randint(-10, 10)
        numerator = str(sympify('(' + linear_func(coeff=coeff, free=free) + ')*(' + linear_func() + ')').expand())
        problem += '({})/({})'.format(numerator, linear_func(coeff=coeff, free=free))
        if coeff==3:
            approach = sympify('{}/{}'.format(-int(free), int(coeff)))
        else:
            approach = str(sympify(-int(free)/int(coeff)))
            approach = approach[::-1]
            number_floats = approach.find('.') + 1
            for i in range(len(approach)):
                if approach[i] == '.':
                    approach = Integer(sympify(approach[::-1]))
                    break
                if approach[i] != '0':
                    approach = sympify(approach[::-1]).round(number_floats-i-1)
                    break
    if level == '3':
        coeff = randint(1, 5)
        sq = choice([1, 4, 9, 16, 25, 36, 49, 64, 81])
        free = randint(-10, 10)
        if coeff == 3:
            approach = sympify(f'({sq}-{free})/{coeff}')
        else:
            approach = str(sympify((sq-int(free))/int(coeff)))
            approach = approach[::-1]
            number_floats = approach.find('.') + 1
            for i in range(len(approach)):
                if approach[i] == '.':
                    approach = Integer(sympify(approach[::-1]))
                    break
                if approach[i] != '0':
                    approach = sympify(approach[::-1]).round(number_floats-i-1)
                    break
        problem += '({})/({} - sqrt({}))'.format(polynomial(), int(sq**0.5), linear_func(coeff=coeff, free=free))
        
    problem = output_func2(sympify(problem))
    approach = output_func2(approach)
    return [problem, approach]


def generateIntegral(level='1'):
    problem = ''
    if level == '1':
        problem += polynomial()
    if level == '2':
        problem += polynomial() + '+{}*'.format(randint(-5, 5)) + trigonometric(1)
    if level == '3':
        problem += polynomial() + '+{}*'.format(randint(-5, 5)) + trigonometric(1) + '+{}*'.format(randint(-5, 5)) + expon(1, 'E') + '+{}*'.format(randint(-5, 5)) + lg(1, 'E')
    if level == '4':
        arc = choice(['1/({}**2+({})**2)'.format(randint(1, 5), linear_func()), 
                    '1/({}**2-({})**2)'.format(randint(1, 5), linear_func()),
                    'x/({})'.format(linear_func())])
        problem += arc + '+{}*'.format(randint(-5, 5)) + expon(1) + '+{}*'.format(randint(-5, 5)) + lg(1)
    problem = sympify(str(sympify(problem)).replace('zoo', '5'))
    problem = output_func2(problem)
    return(problem)

##############################################################################################
# compare function
def compare(user_input:str, answer:str):
    if user_input == answer:
        return True
    else:
        user_input = trigsimp(simplify(parse_func(user_input).expand()))
        answer = trigsimp(simplify(parse_func(answer).expand()))
        if user_input - answer == 0:
            return True
        else:
            return False
print(compare('oo', "oo"))