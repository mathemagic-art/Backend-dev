from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .mathematics import *


@api_view(['POST']) 
def newton_list(request):

    if request.method == 'POST':

        deserialized = String_String_Integer(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['arg_1_str']
            variable = deserialized.data['arg_2_str']
            number_of_iterations = int(deserialized.data['arg_3_int'])
            answer = newton_method(function, variable, number_of_iterations)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:

            return Response(deserialized.error_messages)



@api_view(['POST'])
def diff_list(request):

    if request.method == 'POST':

        deserialized = String_String_Integer(data=request.data)
        
        if deserialized.is_valid():

            function = deserialized.data['arg_1_str']
            variable = deserialized.data['arg_2_str']
            degree = int(deserialized.data['arg_3_int'])

            answer = differentiating_calculator(function, variable, degree)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)
    


@api_view(['POST'])
def taylor_list(request):
    
    if request.method == "POST":

        deserialized = String_String_Integer_Float(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['arg_1_str']
            variable = deserialized.data['arg_2_str']
            number_of_iterations = int(deserialized.data['arg_3_int'])
            center = float(deserialized.data['arg_4_float'])

            answer = taylor_series(function, variable, number_of_iterations, center)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            
            return Response(deserialized.errors)



@api_view(['POST'])
def simpson_list(request):
    
    if request.method == "POST":

        deserialized = String_Float_Float(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['arg_1_str']
            initial_point = float(deserialized.data['arg_2_float'])
            end_point = float(deserialized.data['arg_3_float'])

            answer = taylor_series(function, initial_point, end_point)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(deserialized.errors)



@api_view(['POST',])
def trapezoid_list(request):

    if request.method == 'POST':

        deserialized = String_Float_Float_Integer(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['arg_1_str']
            initial_point = float(deserialized.data['arg_2_float'])
            end_point = float(deserialized.data['arg_3_float'])
            number_interval = int(deserialized.data['arg_4_int'])

            answer = trapezoid_method(function, initial_point, end_point, number_interval)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)



@api_view(['POST',])
def rectangle_list(request):

    if request.method == 'POST':
        deserialized = String_Float_Float_Integer(data=request.data)
        
        if deserialized.is_valid():

            function = deserialized.data['arg_1_str']
            initial_point = float(deserialized.data['arg_2_float'])
            end_point = float(deserialized.data['arg_3_float'])
            number_interval = float(deserialized.data['arg_4_int'])

            answer = rectangle_method(function, initial_point, end_point, number_interval)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)







@api_view(['POST'])
def indefinite_integral_list(request):

    if request.method == 'POST':

        deserialized = String_(data=request.data)
        
        if deserialized.is_valid():

            equation = deserialized.data['arg_1_str']
            answer = indefinite_integration_calculator(equation)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else:
            
            return Response(deserialized.errors)
    





@api_view(['POST'])
def definite_integral_list(request):
    
    if request.method == "POST":
        deserialized = String_Float_Float(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['arg_1_str']
            lower_bound = float(deserialized.data['arg_2_float'])
            upper_bound = float(deserialized.data['arg_3_float'])
            
            answer = definite_integration_calculator(function, lower_bound, upper_bound)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(deserialized.errors)


@api_view(['POST'])
def limit_list(request):
    
    if request.method == "POST":
        deserialized = String_String_String_String(data=request.data)

        if deserialized.is_valid():

            function = deserialized.data['arg_1_str']
            variable = deserialized.data['arg_2_str']
            sign = deserialized.data['arg_3_str']
            approach = deserialized.data['arg_4_str']
            
            answer = limit_calculator(function, variable, sign, approach)
            return Response(answer, status=status.HTTP_201_CREATED)
        
        else: 
            return Response(deserialized.errors)

    

