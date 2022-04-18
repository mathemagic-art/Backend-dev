from rest_framework import serializers


class Function_Numeric_Numeric(serializers.Serializer):
    
    equation = serializers.CharField(max_length=300)
    first = serializers.FloatField()
    second = serializers.FloatField()


class Function(serializers.Serializer):
    
    equation = serializers.CharField(max_length=300)

