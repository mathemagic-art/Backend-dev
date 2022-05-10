from re import search, findall
from math import factorial
from random import choice, randint
from numpy import linspace, random, var
from sympy import Symbol, latex, parse_expr, re, sympify, lambdify, diff, Float, limit, integrate, calculus, S
from scipy import integrate as scipy_integrate
from latex2sympy2 import latex2sympy
import warnings
warnings.filterwarnings("error")
warnings.filterwarnings("ignore", category=UserWarning)
x = Symbol('x')

 
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

# def output_func(function: str) -> str:
#     function = str(function).replace('log', 'ln')
#     function = function.replace('E', 'e')
#     while search('exp\((.*?)\)', function) != None:
#         expression = search('exp\((.*?)\)', function).string
#         ind_of_ln_expr = list(search('exp\((.*?)\)', function).span())
#         ins_exp = findall('exp\((.*?)\)', expression)[0]
#         function = function[:ind_of_ln_expr[0]] + "e**({})".format(ins_exp) + function[ind_of_ln_expr[1]:]
#     while search('ln\((.*?)\)/ln\((.*?)\)', function) != None:
#         expression = search('ln\((.*?)\)/ln\((.*?)\)', function).string
#         ind_of_ln_expr = list(search('ln\((.*?)\)/ln\((.*?)\)', function).span())
#         limit_base, limit_expr = findall('ln\((.*?)\)', expression)
#         function = function[:ind_of_ln_expr[0]] + "log({},{})".format(limit_base, limit_expr) + function[ind_of_ln_expr[1]:]
#     return function

# def parse_func2(function: str): 
#     function = function.replace('\frac', '\\frac')
#     function = function.replace('\tan', '\\tan')
#     function = function.replace('\arcsin', '\\arcsin')
#     function = function.replace('\arccos', '\\arccos')
#     function = function.replace('\arctan', '\\arctan')
#     function = function.replace('\arccot', '\\arccot')
#     function = latex_to_sympy(function) 
#     return function



def output_func(function: str): ## consider the case when we are multiplying function with log [sin(x)*log(x)]/[log(3)] or [x**2*log(x)]/[sin(x)*log(2)]
    function = latex(sympify(function))
    function = str(function).replace('log', 'ln')
  
    # copy_func = function    #this part of code does not work stable
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
    #     function = function[:ind_of_expr[0]] + "\\frac{{{}}}{{{}}}\\log_{} ({})".format(coeff1, coeff2, edit_inner_func(log_base), edit_inner_func(log_expr)) + function[key_ind+1:] 
    #     copy_func = function
    return function

#print(output_func2('(3*log(x))/(4*log(3))'))
########################################################################################################################


def differentiating_calculator(function: str, variable: str, degree: int) -> str:    
    function = parse_func(function)
    degree = int(degree)
    variable = Symbol(variable)
    function_prime = function.diff(variable, degree)  
    ans = output_func(function_prime)
    return ans
########################################################################################################################

def taylor_series(function:str, variable: str, number_of_iterations: int, center: float) -> str:

    number_of_iterations = int(number_of_iterations)
    center = float(center)

    function = parse_func(function)
    variable = Symbol(variable)

    if center == 0:
        taylorPolynomial = str(lambdify(variable, function)(center))
        for i in range(1, number_of_iterations):
            f_diff = str(lambdify(variable, diff(function, variable, i))(center))
            taylorPolynomial += '+' + f_diff +'/'+str(factorial(i))+'*({}-{})**{}'.format(variable, center, i)    
        taylorPolynomial = sympify(taylorPolynomial, rational=True)
    else:
        taylorPolynomial = str(function.subs(variable, center))
        for i in range(1, number_of_iterations):
            f_diff = diff(function, variable, i)
            f_diff = str(f_diff.subs(variable, center))
            taylorPolynomial += '+' + f_diff +'/'+str(factorial(i))+'*({}-{})**{}'.format(variable, center, i)    
        taylorPolynomial = sympify(taylorPolynomial, rational=True)
    
    return output_func(taylorPolynomial)

########################################################################################################################


def newton_method(function: str, variable: str, number_of_iterations: int) -> str:

    number_of_iterations = int(number_of_iterations)
    try:
        function = parse_func(function)
        variable = Symbol(variable)
        f = lambdify(variable, function) #lambdify expression of the input function
        f_d = lambdify(variable, diff(function, variable))  #lambdify expression of the derivative of the input function
        interval = findall('Interval.*?\(.*?\)',  str(calculus.util.continuous_domain(function, variable, S.Reals))) #checking the domain
        if interval: 
            interval = interval[0]
            interval = findall('\(.*?\)', interval)[0][1:-1].split(',')
            if interval[0] == '-oo':
                x_i = int(interval[1]) - 1
            elif interval[1] == 'oo':
                x_i = int(interval[0]) + 1
            else:
                x_i = int(interval[0]) + (int(interval[1]) - int(interval[0]))/2
        else:
            x_i = random.randint(1, 10)
        for i in range(int(number_of_iterations)):
            x_i = x_i - (f(x_i)/f_d(x_i))
        ret = str(Float(x_i).round(4))
        if '.0000' in ret:
            ret = ret[:ret.index('.')]
        return ret
    except RuntimeWarning:
        return "Something went wrong. Please check the criteria."

########################################################################################################################


def simpsons_method(function: str, variable: str, initial_point: float, end_point: float) -> str:

    variable = Symbol(variable)
    initial_point = float(initial_point)
    end_point = float(end_point)

    def find_polynomial(x1, x2, x3, y1, y2, y3):
     
        a = (x1*(y3-y2) + x2*(y1-y3) + x3*(y2-y1))/((x1-x2)*(x1-x3)*(x2-x3))
        b = ((y2-y1)/(x2-x1)) - a*(x1+x2) 
        c = (y1 - a*x1**2 - b*x1)
     
        return lambdify(x, sympify('{}*x**2 + {}*x + {}'.format(a, b, c)))
    
    n = random.randint(5, 50)
    function = parse_func(function)
    function = lambdify(x, function)
    
    if n % 2 != 0:
        n += 1
    
    x_values = linspace(initial_point, end_point, n+1)
    dx = (end_point-initial_point)/n
    Area = 0
    
    for i in range(0, len(x_values)-2, 2):
        
        x_1, x_2, x_3 = x_values[i], x_values[i+1], x_values[i+2] 
        pol_func = find_polynomial(x_1, x_2, x_3, function(x_1), function(x_2), function(x_3))
        Area += scipy_integrate.quad(pol_func ,x_1, x_3)[0]
        
    return str(Float(Area).round(4)) if '.0000' not in str(Float(Area).round(4)) else str(Float(Area).round(4))[:str(Float(Area).round(4)).index('.')]

########################################################################################################################


def trapezoid_method(function: str, variable: str, initial_point: float, end_point: float, number_of_intervals: int) -> str:

    variable = Symbol(variable)
    initial_point = float(initial_point)
    end_point = float(end_point)
    number_of_intervals = int(number_of_intervals)
    function = parse_func(function)
    function = lambdify(variable, function)

    dx = (end_point - initial_point)/number_of_intervals
    A = 1/2 *(function(initial_point) + function(end_point))
    for i in range(1, number_of_intervals):
        A = A + function(initial_point + i*dx)
    Area = dx * A
    return str(Float(Area).round(4)) if '.0000' not in str(Float(Area).round(4)) else str(Float(Area).round(4))[:str(Float(Area).round(4)).index('.')]

########################################################################################################################


def midpoint_method(function:str, variable: str, initial_point: float, end_point: float, number_of_intervals: int) -> str:

    variable = Symbol(variable)
    initial_point = float(initial_point)
    end_point = float(end_point)
    number_of_intervals = int(number_of_intervals)
    x_val = linspace(initial_point, end_point, number_of_intervals+1)
    function = parse_func(function)
    function = lambdify(variable, function)
    dx = (end_point - initial_point)/number_of_intervals
    total = 0.0

    for i in range(len(x_val)-1):
        total += dx*function((x_val[i]+x_val[i+1])/2)


    return str(Float(total).round(4)) if '.0000' not in str(Float(total).round(4)) else str(Float(total).round(4))[:str(Float(total).round(4)).index('.')]
########################################################################################################################


def definite_integration_calculator(function: str, variable: str, initial_point: float, end_point: float) -> str:
    variable = Symbol(variable)
    initial_point = float(initial_point)
    end_point = float(end_point)

    function = parse_func(function)
    a = lambdify(variable, integrate(sympify(function), variable)) 
    return str(Float(a(end_point)-a(initial_point)).round(5))



def indefinite_integration_calculator(function: str, variable: str) -> str:
    
    variable = Symbol(variable)
    function = parse_func(function)
    ans = integrate(function, variable)

    return output_func(ans)




def limit_calculator(function: str, variable : str, sign: str, approach: str) -> str:
    
    variable = Symbol(variable)
    function = parse_func(function)
    
    if sign == '+' or sign == '-':        
        ans = str(sympify(limit(function, variable, approach, sign)).evalf())    
    else:
        ans = str(sympify(limit(function, variable, approach)).evalf())
    if 'oo' in ans:
        return ans
    else:
        return str(Float(ans).round(4)) if '.0000' not in str(Float(ans).round(4)) else str(Float(ans).round(4))[:str(Float(ans).round(4)).index('.')]
       
########################################################################################################################

def universal_integral(type: str, function: str, variable: str, initial_point: float, end_point: float):
    if type == "definite":
        variable = Symbol(variable)
        initial_point = float(initial_point)
        end_point = float(end_point)
        function = parse_func(function)
        a = lambdify(variable, integrate(sympify(function), variable)) 
        return output_func("{:.5f}".format(a(end_point)-a(initial_point)))
    else:
        variable = Symbol(variable)
        function = parse_func(function)
        ans = integrate(function, variable)
        return output_func(ans)

#########################################################################################################################
