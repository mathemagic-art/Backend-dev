from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NewtonSerializer, DiffSerializer
from .mathematics import newtonMethod, diffMethod

@api_view(['POST'])
def diff_list(request):
    if request.method == 'POST':
        deserialized = DiffSerializer(data=request.data)

        if deserialized.is_valid():
            equation = deserialized.data['equation']
            answer = diffMethod(equation)

            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)


@api_view(['POST'])
def newton_list(request):
    if request.method == 'POST':
        deserialized = NewtonSerializer(data=request.data)
        if deserialized.is_valid():
            equation = deserialized.data['equation']
            first = int(deserialized.data['first'])
            second = int(deserialized.data['second'])
            answer = newtonMethod(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)