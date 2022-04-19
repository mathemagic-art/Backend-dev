import sympy as sp 
import numpy as np
import math
import warnings
import scipy.integrate

warnings.filterwarnings("error")
warnings.filterwarnings("ignore", category=UserWarning)
x = sp.Symbol('x')

########################################################################################################################
# done by Shokhrukh

def newton_method(input_function: str, first_guess: int, number_of_iterations: int) -> str:
    try:
        input_function = sp.sympify(input_function.replace('e', 'E')) #replaces 
        f = sp.lambdify(x, input_function) #lambdify expression of the input function
        f_d = sp.lambdify(x, sp.diff(input_function, x))  #lambdify expression of the derivative of the input function
        x_i = first_guess
        for i in range(number_of_iterations):
            x_i = x_i - (f(x_i)/f_d(x_i))
        if f(x_i) > 0.000001:
            return "Please check the function. Probably, it does not have any roots"
        else:
            return str(x_i)
    except RuntimeWarning:
        return "Please change your first guess. Perhaps, the method came across with vertex or new x_i are diverging instead of converging."



########################################################################################################################
#Done by Aisha

def differentiating_calculator(function: str) -> str:

    function = function.replace('e', 'E')
    function = sp.sympify(function)
    function_prime = function.diff(x)  
    function = sp.lambdify(x, function) 

    return str(function_prime)



########################################################################################################################
# done by Tariq

def rectangle_method(function:str, init_point:int, end_point:int, num_of_interval:int)->str:
  
    x = sp.symbols('x')
    function = sp.lambdify(x, function)
    dx = (end_point - init_point)/num_of_interval
    total = 0.0

    for i in range (num_of_interval):
        total = total + function((init_point + (i*dx)))

    area = dx*total

    return str(area) 

########################################################################################################################
#  by Attullah

def taylor_series(function, num_of_iter, center):
    
    function = function.replace('e', 'E')
    taylorPolynomial = str(sp.lambdify(x, sp.sympify(function))(center))
    
    for i in range(1, num_of_iter):
        f_diff = str(sp.lambdify(x, sp.diff(function, x, i))(center))
        taylorPolynomial += '+' + f_diff +'/'+str(math.factorial(i))+'*(x-{})**{}'.format(center, i)
    
    taylorPolynomial = sp.sympify(taylorPolynomial, rational=True)
    
    return str(taylorPolynomial)



########################################################################################################################
# Zakir and Tariq

def simpsons_method(function: str, initial_point: int, end_point: int)->str:

    def find_polynomial(x1, x2, x3, y1, y2, y3):
     
        a = (x1*(y3-y2) + x2*(y1-y3) + x3*(y2-y1))/((x1-x2)*(x1-x3)*(x2-x3))
        b = ((y2-y1)/(x2-x1)) - a*(x1+x2) 
        c = y1 - a*x1**2 - b*x1
     
        return sp.lambdify(x, sp.sympify('{}*x**2 + {}*x + {}'.format(a, b, c)))
    
    n = np.random.randint(5, 50)
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
        
    return str(Area)   


####################################################################################################
# by Shokhrukh 

def trapezoid_method(function:str,initial_point:int,end_point:int,number_interval:int) ->str:
  function = sp.lambdify(x, function)
  dx = (end_point - initial_point)/number_interval
  A = 1/2 *(function(initial_point) + function(end_point))
  for i in range(1, number_interval):
      A = A + function(initial_point + i*dx)
  Area = dx * A
  return str(Area)


##############################################################################################################

def rectangle_method(function:str, initial_point:int, end_point:int, num_of_interval:int)->str:
  function = sp.lambdify(x, function)
  dx = (end_point - initial_point)/num_of_interval
  total = 0.0
  for i in range (num_of_interval):
          total = total + function((initial_point + (i*dx)))
  Area = dx*total
  return str(Area) 

