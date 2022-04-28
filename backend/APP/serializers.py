from rest_framework import serializers

class string(serializers.Serializer):
    equation = serializers.CharField(max_length=300)


class Function_Two_Numeric(serializers.Serializer):
    
    
    first = serializers.FloatField()
    second = serializers.FloatField()

class Function_Three_Numeric(serializers.Serializer):

    equation = serializers.CharField(max_length=300)
    first = serializers.FloatField()
    second = serializers.FloatField()
    third = serializers.FloatField()

class Function_Two_String(serializers.Serializer):
    equation = serializers.CharField(max_length=300)
    first = serializers.CharField(max_length=300)
    second = serializers.CharField(max_length=300)

class Function_String_Numeric(serializers.Serializer):
    equation = serializers.CharField(max_length=300)
    first = serializers.CharField(max_length=300)
    second = serializers.IntegerField()

class string_string_int_float(serializers.Serializer):
    equation = serializers.CharField(max_length=300)
    first = serializers.CharField(max_length=300)
    second = serializers.IntegerField()
    third = serializers.FloatField()