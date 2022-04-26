from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .mathematics import *


@api_view(['POST']) 
def newton_list(request):

    if request.method == 'POST':

        deserialized = Function_String_Numeric(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = deserialized.data['first']
            second = int(deserialized.data['second'])
            answer = newton_method(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:

            return Response(deserialized.error_messages)



@api_view(['POST'])
def diff_list(request):

    if request.method == 'POST':

        deserialized = Function(data=request.data)
        
        if deserialized.is_valid():

            equation = deserialized.data['equation']
            answer = differentiating_calculator(equation)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)
    


@api_view(['POST'])
def taylor_list(request):
    
    if request.method == "POST":

        deserialized = Function_Two_Numeric(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = float(deserialized.data['first'])
            second = float(deserialized.data['second'])
            
            answer = taylor_series(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            
            return Response(deserialized.errors)



@api_view(['POST'])
def simpson_list(request):
    
    if request.method == "POST":
        deserialized = Function_Two_Numeric(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = float(deserialized.data['first'])
            second = float(deserialized.data['second'])
            
            answer = simpsons_method(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(deserialized.errors)



@api_view(['POST',])
def trapezoid_list(request):

    if request.method == 'POST':
        deserialized = Function_Three_Numeric(data=request.data)

        if deserialized.is_valid():
            equation = deserialized.data['equation']
            first = float(deserialized.data['first'])
            second = float(deserialized.data['second'])
            third = float(deserialized.data['third'])

            answer = trapezoid_method(equation, first, second, third)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)



@api_view(['POST',])
def rectangle_list(request):

    if request.method == 'POST':
        deserialized = Function_Three_Numeric(data=request.data)
        
        if deserialized.is_valid():
            equation = deserialized.data['equation']
            first = float(deserialized.data['first'])
            second = float(deserialized.data['second'])
            third = float(deserialized.data['third'])

            answer = rectangle_method(equation, first, second, third)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)



@api_view(['POST'])
def definite_integral_list(request):
    
    if request.method == "POST":
        deserialized = Function_Two_Numeric(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = float(deserialized.data['first'])
            second = float(deserialized.data['second'])
            
            answer = definite_integration_calculator(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(deserialized.errors)


@api_view(['POST'])
def limit_list(request):
    
    if request.method == "POST":
        deserialized = Function_Two_String(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = deserialized.data['first']
            second = deserialized.data['second']
            
            answer = limit_calculator(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(deserialized.errors)