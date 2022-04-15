from rest_framework import serializers


class Function_Integer_Integer(serializers.Serializer):
    
    equation = serializers.CharField(max_length=300)
    first = serializers.IntegerField()
    second = serializers.IntegerField()


class Function(serializers.Serializer):
    
    equation = serializers.CharField(max_length=300)

