from rest_framework import serializers


class String_(serializers.Serializer):
    
    argument_1 = serializers.CharField(max_length=300)


class String_String_(serializers.Serializer):
    
    argument_1 = serializers.CharField(max_length=300)
    argument_2 = serializers.CharField(max_length=300)


class String_String_String_(serializers.Serializer):
    
    argument_1 = serializers.CharField(max_length=300)
    argument_2 = serializers.CharField(max_length=300)
    argument_3 = serializers.CharField(max_length=300)


class String_String_String_String_(serializers.Serializer):
    
    argument_1 = serializers.CharField(max_length=300)
    argument_2 = serializers.CharField(max_length=300)
    argument_3 = serializers.CharField(max_length=300)
    argument_4 = serializers.CharField(max_length=300)