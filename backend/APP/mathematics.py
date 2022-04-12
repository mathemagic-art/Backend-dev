from sympy import *
from numpy import random
x = Symbol('x')
import warnings
warnings.filterwarnings("error")
warnings.filterwarnings("ignore", category=UserWarning)

def newtonMethod(input_function, first_guess, number_of_iterations):
    try:
        input_function = sympify(input_function.replace('e', 'E')) #replaces 
        f = lambdify(x, input_function) #lambdify expression of the input function
        f_d = lambdify(x, diff(input_function, x))  #lambdify expression of the derivative of the input function
        x_i = first_guess
        for i in range(number_of_iterations):
            x_i = x_i - (f(x_i)/f_d(x_i))
        if f(x_i) > 0.000001:
            return "Please check the function. Probably, it does not have any roots"
        else:
            return x_i
    except RuntimeWarning:
        return "Please change your first guess. Perhaps, the method came across with vertex or new x_i are diverging instead of converging."





# We have to create a "symbol" called x, as you will have any (a,h or y variables) you should write 'var = Symbol ('var')' and ect
def diffMethod(f):
    
    x = Symbol('x') #these are variables
    f = f.replace('e', 'E')
    f = sympify(f) #this is input (be careful with writing the power of exp, because here we dont use usal (**) but just take in breakets 
    f_prime = f.diff(x)  
    f = lambdify(x, f) #idetifiying respect to which variable we are taking variable
    #print in the space (f_prime) it will give the answer
    return str(f_prime)