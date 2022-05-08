from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .calculators import *
from .test_generators import *


@api_view(['POST'])
def differentiation_api(request):

    if request.method == 'POST':

        deserialized = String_String_String_(data=request.data)
        
        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']
            degree = deserialized.data['argument_3']

            answer = differentiating_calculator(function, variable, degree)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)


@api_view(['POST'])
def taylors_method_api(request):
    
    if request.method == "POST":

        deserialized = String_String_String_String_(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']
            number_of_iterations = deserialized.data['argument_3']
            center = deserialized.data['argument_4']

            answer = taylor_series(function, variable, number_of_iterations, center)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            
            return Response(deserialized.errors)


@api_view(['POST']) 
def newtons_method_api(request):

    if request.method == 'POST':

        deserialized = String_String_String_(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']
            number_of_iterations = deserialized.data['argument_3']

            answer = newton_method(function, variable, number_of_iterations)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:

            return Response(deserialized.error_messages)


@api_view(['POST'])
def simpsons_method_api(request):
    
    if request.method == "POST":

        deserialized = String_String_String_String_(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']
            initial_point = deserialized.data['argument_3']
            end_point = deserialized.data['argument_4']
            
            answer = simpsons_method(function,variable, initial_point, end_point)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(deserialized.errors)


@api_view(['POST',])
def trapezoid_method_api(request):

    if request.method == 'POST':
        deserialized = String_String_String_String_String_(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']
            initial_point = deserialized.data['argument_3']
            end_point = deserialized.data['argument_4']
            number_interval = deserialized.data['argument_5']
            answer = trapezoid_method(function, variable, initial_point, end_point, number_interval)

            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)



@api_view(['POST',])
def rectangle_method_api(request):

    if request.method == 'POST':
        deserialized = String_String_String_String_String_(data=request.data)

        
        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']
            initial_point = deserialized.data['argument_3']
            end_point = deserialized.data['argument_4']
            number_interval = deserialized.data['argument_5']
            answer = rectangle_method(function, variable , initial_point, end_point, number_interval)
            
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)


@api_view(['POST'])
def definite_integral_api(request):
    
    if request.method == "POST":
        deserialized = String_String_String_String_(data=request.data)
    
        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']
            initial_point = deserialized.data['argument_3']
            end_point = deserialized.data['argument_4']
            
            answer = definite_integration_calculator(function, variable, initial_point, end_point)

            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)

            
@api_view(['POST'])
def indefinite_integral_api(request):


        deserialized = String_String_(data=request.data)
        
        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']

            answer = indefinite_integration_calculator(function, variable)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)

@api_view(['POST'])
def limit_api(request):
    
    if request.method == "POST":
        deserialized = String_String_String_String_(data=request.data)

        if deserialized.is_valid():
            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']
            sign = deserialized.data['argument_3']
            approach = deserialized.data['argument_4']
            
            answer = limit_calculator(function, variable, sign, approach)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(deserialized.errors)

@api_view(['POST'])
def universal_integral_api(request):   
    if request.method == "POST":
        deserialized = String_String_String_String_String_(data=request.data)
    
        if deserialized.is_valid():
            type = deserialized.data['argument_1']
            function = deserialized.data['argument_2']
            variable = deserialized.data['argument_3']
            initial_point = deserialized.data['argument_4']
            end_point = deserialized.data['argument_5']
            
            answer = universal_integral(type, function, variable, initial_point, end_point)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)


@api_view(['POST'])
def test_differentiation_api(request):
        deserialized = String_(data=request.data)
        if deserialized.is_valid():
            level = deserialized.data['argument_1']
            answer = generateDifferentiation(level)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.errors)
            

@api_view(['POST'])
def test_indefinite_integral_api(request):
        deserialized = String_(data=request.data)
        if deserialized.is_valid():
            level = deserialized.data['argument_1']
            answer = generateIntegral(level)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.errors)

