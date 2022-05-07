from pydoc import apropos
from random import choice, randint, choices
from regex import E
from scipy import rand
from sympy import Symbol, sympify, Symbol, oo, Integer

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
        problem = 'log({}, {})'.format(polynomial,base)
    return problem

######################################################################################
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
    return sympify(str(sympify(problem)).replace('zoo', '5'))


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
    return sympify(problem), approach

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
    return sympify(str(sympify(problem)).replace('zoo', '5'))