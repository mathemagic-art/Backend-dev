import re
from re import search, findall
from math import factorial
from numpy import linspace, random, var
from sympy import Symbol, sympify, lambdify, diff, Float, limit, integrate, calculus, S
from scipy import integrate as scipy_integrate
import warnings
warnings.filterwarnings("error")
warnings.filterwarnings("ignore", category=UserWarning)
x = Symbol('x')

########################################################################################################################
# parsing and output functions 
 
def parse_func(function: str):

    return sympify(function.replace('e', 'E'), convert_xor=True)

def output_func(function: str) -> str:
    function = str(function).replace('log', 'ln')
    function = function.replace('E', 'e')
    while search('exp\((.*?)\)', function) != None:
        expression = search('exp\((.*?)\)', function).string
        ind_of_ln_expr = list(search('exp\((.*?)\)', function).span())
        ins_exp = findall('exp\((.*?)\)', expression)[0]
        function = function[:ind_of_ln_expr[0]] + "e**({})".format(ins_exp) + function[ind_of_ln_expr[1]:]
    while search('ln\((.*?)\)/ln\((.*?)\)', function) != None:
        expression = search('ln\((.*?)\)/ln\((.*?)\)', function).string
        ind_of_ln_expr = list(search('ln\((.*?)\)/ln\((.*?)\)', function).span())
        limit_base, limit_expr = findall('ln\((.*?)\)', expression)
        function = function[:ind_of_ln_expr[0]] + "log({},{})".format(limit_base, limit_expr) + function[ind_of_ln_expr[1]:]
    return function

########################################################################################################################

def newton_method(function: str, variable: str, number_of_iterations: int) -> str:

    number_of_iterations = int(number_of_iterations)
    try:
        function = parse_func(function)
        variable = Symbol(variable)
        f = lambdify(variable, function) #lambdify expression of the input function
        f_d = lambdify(variable, diff(function, variable))  #lambdify expression of the derivative of the input function
        interval = re.findall('Interval.*?\(.*?\)',  str(calculus.util.continuous_domain(function, variable, S.Reals))) #checking the domain
        if interval: 
            interval = interval[0]
            interval = re.findall('\(.*?\)', interval)[0][1:-1].split(',')
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

def differentiating_calculator(function: str, variable: str, degree: int) -> str:
    
    degree = int(degree)

    function = parse_func(function)
    variable = Symbol(variable)
    function_prime = function.diff(variable, degree)  
    ans = output_func(function_prime)
    return ans
########################################################################################################################

def indefinite_integration_calculator(function: str, variable: str) -> str:
    
    variable = Symbol(variable)
    function = parse_func(function)
    ans = lambdify(variable, integrate(sympify(function)))

    return output_func(ans)

########################################################################################################################

def definite_integration_calculator(function: str, variable: str, initial_point: float, end_point: float) -> str:
    variable = Symbol(variable)
    initial_point = float(initial_point)
    end_point = float(end_point)

    function = parse_func(function)
    a = lambdify(variable, integrate(sympify(function), variable)) 
    return output_func("{:.5f}".format(a(end_point)-a(initial_point)))

#########################################################################################################################


def limit_calculator(function: str, variable : str, sign: str, approach: str) -> str:
    
    variable = Symbol(variable)
    function = parse_func(function)
    
    if len(sign) == 1:        

        ans = str(sympify(limit(function, variable, approach, sign)).evalf())
        if 'oo' in ans:
            return ans
        else:
            return '{:.5f}'.format(float(ans))
    else:
        ans = str(sympify(limit(function, variable, approach)).evalf())
        if 'oo' in ans:
            return ans
        else:
            return '{:.5f}'.format(float(ans))
            
########################################################################################################################

def rectangle_method(function:str, variable: str, initial_point: float, end_point: float, number_of_intervals: int) -> str:

    variable = Symbol(variable)
    initial_point = float(initial_point)
    end_point = float(end_point)
    number_of_intervals = int(number_of_intervals)

    function = parse_func(function)
    function = lambdify(variable, function)
    dx = (end_point - initial_point)/number_of_intervals
    total = 0.0

    for i in range (number_of_intervals):
        total = total + function((initial_point + (i*dx)))

    area = dx*total

    return "{:.5f}".format(area)

#######################################################################################################################

def simpsons_method(function: str, variable: str, initial_point: float, end_point: float) -> str:

    variable = Symbol(variable)
    initial_point = float(initial_point)
    end_point = float(end_point)

    def find_polynomial(x1, x2, x3, y1, y2, y3):
     
        a = (x1*(y3-y2) + x2*(y1-y3) + x3*(y2-y1))/((x1-x2)*(x1-x3)*(x2-x3))
        b = ((y2-y1)/(x2-x1)) - a*(x1+x2) 
        c = y1 - a*x1**2 - b*x1
     
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
        
    return "{:.5f}".format(Area)   

######################################################################################################################

def trapezoid_method(function: str, variable: str, initial_point: float, end_point: float, number_of_intervals: int) -> str:

    variable = Symbol(variable)
    initial_point = float(initial_point)
    end_point = float(end_point)
    number_of_intervals = int(number_of_intervals)

    function = lambdify(x, function)
    dx = (end_point - initial_point)/number_of_intervals
    A = 1/2 *(function(initial_point) + function(end_point))
    for i in range(1, number_of_intervals):
        A = A + function(initial_point + i*dx)
    Area = dx * A
    return "{:.5f}".format(Area)

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