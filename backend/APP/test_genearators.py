from random import choice, randint
def generateDifferentiation(level:str):

    # dependencies
    problem = ''
    types = {
        'Trigonometric': ['sin', 'cos', 'tan', 'cot', 'sec'],
        'Exponential': ['e'],
        'Logarithmic': ['ln']
    }
    operators = ["+", "-", "*", "/"]
    random_operator = choice(operators)

    # layouts
    def polynomial():
        coeff = randint(2, 5)
        power = randint(2, 5)
        problem = "{}*x**{}".format(coeff, power)
        return problem

    def trigonometric():
        coeff_1 = randint(2, 5)
        coeff_2 = randint(2, 5)
        func_type = list(types.keys())[0]
        func = choice(types[func_type])
        problem = "({}*{}*({}*x))".format(coeff_1, func, coeff_2)
        return problem

    # logic
    if level == '1':
        problem += "({}){}({})".format(polynomial(),
                                       random_operator, polynomial())

    if level == '2':
        problem += "({}){}({})".format(trigonometric(),
                                       random_operator, trigonometric())

    if level == '3':
        coeff_1 = randint(2, 5)
        coeff_2 = randint(2, 5)
        power_1 = randint(2, 5)
        func_type = choice(list(types.keys())[1:])
        func = types[func_type][0]

        if func == 'e':
            problem += "{}*{}**({}*x**{})".format(
                polynomial(), func, coeff_2, power_1)
        else:
            problem += "{}*{}*({}){}{}".format(
                coeff_1, func, polynomial(), random_operator, trigonometric())

    return problem
