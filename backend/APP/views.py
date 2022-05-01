from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .mathematics import *


@api_view(['POST'])
def diff_list(request):

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
def taylor_list(request):
    
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
def newton_list(request):

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
def simpson_list(request):
    
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
def trapezoid_list(request):

    if request.method == 'POST':

        deserialized = String_String_String_String_String(data=request.data)

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
def rectangle_list(request):

    if request.method == 'POST':
        deserialized = String_String_String_String_(data=request.data)
        
        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            initial_point = deserialized.data['argument_2']
            end_point = deserialized.data['argument_3']
            number_interval = deserialized.data['argument_4']

            answer = rectangle_method(function, initial_point, end_point, number_interval)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)


@api_view(['POST'])
def definite_integral_list(request):
    
    if request.method == "POST":
        deserialized = String_String_String_String_(data=request.data)

        deserialized = String_String_(data=request.data)
        
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
def indefinite_integral_list(request):


        deserialized = String_String_(data=request.data)
        
        if deserialized.is_valid():

            function = deserialized.data['argument_1']
            variable = deserialized.data['argument_2']

            answer = indefinite_integration_calculator(function, variable)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)


@api_view(['POST'])
def limit_list(request):
    
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