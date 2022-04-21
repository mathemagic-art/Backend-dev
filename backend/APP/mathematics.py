import re
import sympy as sp 
import numpy as np
import math
import warnings
import scipy.integrate
warnings.filterwarnings("error")
warnings.filterwarnings("ignore", category=UserWarning)
x = sp.Symbol('x')

########################################################################################################################
# parsing and output functions 
 
def parse_func(function: str):
    return sp.sympify(function.replace('e', 'E'), convert_xor=True)

def output_func(function):
    function = str(function).replace('log', 'ln')
    while re.search('ln\((.*?)\)/ln\((.*?)\)', function) != None:
        expression = re.search('ln\((.*?)\)/ln\((.*?)\)', function).string
        ind_of_ln_expr = list(re.search('ln\((.*?)\)/ln\((.*?)\)', function).span())
        limit_base, limit_expr = re.findall('ln\((.*?)\)', expression)
        function = function[:ind_of_ln_expr[0]] + "log({},{})".format(limit_base, limit_expr) + function[ind_of_ln_expr[1]:]
    return function

########################################################################################################################

def newton_method(input_function: str, first_guess: int, number_of_iterations: int) -> str:
    try:
        input_function = parse_func(input_function) #replaces 
        f = sp.lambdify(x, input_function) #lambdify expression of the input function
        f_d = sp.lambdify(x, sp.diff(input_function, x))  #lambdify expression of the derivative of the input function
        x_i = first_guess
        for i in range(number_of_iterations):
            x_i = x_i - (f(x_i)/f_d(x_i))
        if f(x_i) > 0.000001:
            return "It seems that you put unsufficient number of iterations. Please make it bigger. Also, check the function. Probably, it does not have any roots."
        else:
            return str(x_i)
    except RuntimeWarning:
        return "Please change your first guess. Perhaps, the method came across with vertex or new x_i are diverging instead of converging."

########################################################################################################################

def differentiating_calculator(function: str) -> str:

    function = parse_func(function)
    function_prime = function.diff(x)  
    return output_func(function_prime)

########################################################################################################################

def indefinite_integration_calculator(function: str) -> str:
  return output_func(sp.integrate(parse_func(function)))

########################################################################################################################

def definite_integration_calculator(function:str, lower_bound:int, upper_bound:int) -> str:
  function = parse_func(function)
  a = sp.lambdify(x, sp.integrate(sp.sympify(function))) 
  return output_func("{:.5f}".format(a(upper_bound)-a(lower_bound)))

#########################################################################################################################

def limit_calculator(function: str, symbol : str, approach: str) -> str:
    function = parse_func(function)    
    if approach[-1] in ['+', '-']:        
        sign = approach[-1]
        approach = int(approach[:-1])
        ans = str("{}".format(sp.sympify(sp.limit(function, symbol, approach, sign)).evalf()))
    else:
        if approach.isdigit():
            approach = int(approach)
    
        ans = str("{:.5f}".format(sp.sympify(sp.limit(function, symbol, approach)).evalf()))    
    
    
    return str(ans)

########################################################################################################################

def rectangle_method(function:str, init_point:int, end_point:int, num_of_interval:int)->str:
    function = parse_func(function)
    function = sp.lambdify(x, function)
    dx = (end_point - init_point)/num_of_interval
    total = 0.0

    for i in range (num_of_interval):
        total = total + function((init_point + (i*dx)))

    area = dx*total

    return "{:.5f}".format(area)

#######################################################################################################################

def simpsons_method(function: str, initial_point: int, end_point: int)-> str:

    def find_polynomial(x1, x2, x3, y1, y2, y3):
     
        a = (x1*(y3-y2) + x2*(y1-y3) + x3*(y2-y1))/((x1-x2)*(x1-x3)*(x2-x3))
        b = ((y2-y1)/(x2-x1)) - a*(x1+x2) 
        c = y1 - a*x1**2 - b*x1
     
        return sp.lambdify(x, sp.sympify('{}*x**2 + {}*x + {}'.format(a, b, c)))
    
    n = np.random.randint(5, 50)
    function = parse_func(function)
    function = sp.lambdify(x, function)
    
    if n % 2 != 0:
        n += 1
    
    x_values = np.linspace(initial_point, end_point, n+1)
    dx = (end_point-initial_point)/n
    Area = 0
    
    for i in range(0, len(x_values)-2, 2):
        
        x_1, x_2, x_3 = x_values[i], x_values[i+1], x_values[i+2] 
        pol_func = find_polynomial(x_1, x_2, x_3, function(x_1), function(x_2), function(x_3))
        Area += scipy.integrate.quad(pol_func ,x_1, x_3)[0]
        
    return "{:.5f}".format(Area)   

######################################################################################################################

def trapezoid_method(function:str,initial_point:int,end_point:int,number_interval:int) ->str:
  function = sp.lambdify(x, function)
  dx = (end_point - initial_point)/number_interval
  A = 1/2 *(function(initial_point) + function(end_point))
  for i in range(1, number_interval):
      A = A + function(initial_point + i*dx)
  Area = dx * A
  return "{:.5f}".format(Area)

########################################################################################################################

def taylor_series(function, num_of_iter, center) -> str:
    
    function = parse_func(function)
    taylorPolynomial = str(sp.lambdify(x, function)(center))
    
    for i in range(1, num_of_iter):
        f_diff = str(sp.lambdify(x, sp.diff(function, x, i))(center))
        taylorPolynomial += '+' + f_diff +'/'+str(math.factorial(i))+'*(x-{})**{}'.format(center, i)
    
    taylorPolynomial = sp.sympify(taylorPolynomial, rational=True)
    
    return output_func(taylorPolynomial)
