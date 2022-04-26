from ast import arguments
from rest_framework import serializers


class String_String_Integer(serializers.Serializer):
    
    arg_1_str = serializers.CharField(max_length=300)
    arg_2_str = serializers.CharField(max_length=300)
    arg_3_int = serializers.IntegerField()


class String_Float_Float(serializers.Serializer):
    
    arg_1_str = serializers.CharField(max_length=300)
    arg_2_float = serializers.FloatField()
    arg_3_float = serializers.FloatField()


class String_Integer_Float(serializers.Serializer):
    
    arg_1_str = serializers.CharField(max_length=300)
    arg_2_int = serializers.IntegerField()
    arg_3_float = serializers.FloatField()


class String_Float_Float_Integer(serializers.Serializer):

    arg_1_str = serializers.CharField(max_length=300)
    arg_2_float = serializers.FloatField()
    arg_3_float = serializers.FloatField()
    arg_4_int = serializers.IntegerField()


class String_String_String(serializers.Serializer):
    
    arg_1_str = serializers.CharField(max_length=300)
    arg_2_str = serializers.CharField(max_length=300)
    arg_3_str = serializers.CharField(max_length=300)
       