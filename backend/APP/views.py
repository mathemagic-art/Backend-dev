from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .mathematics import *
# Create your views here.

@api_view(['POST'])
def newton_list(request):

    if request.method == 'POST':

        deserialized = Function_Numeric_Numeric(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = int(deserialized.data['first'])
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

        deserialized = Function_Numeric_Numeric(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = int(deserialized.data['first'])
            second = int(deserialized.data['second'])
            
            answer = taylor_series(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            
            return Response(deserialized.errors)

@api_view(['POST'])
def simpson_list(request):
    
    if request.method == "POST":

        deserialized = Function_Numeric_Numeric(data=request.data)

        if deserialized.is_valid():

            equation = deserialized.data['equation']
            first = int(deserialized.data['first'])
            second = int(deserialized.data['second'])
            
            answer = simpsons_method(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            
            return Response(deserialized.errors)
