from rest_framework import serializers


class NewtonSerializer(serializers.Serializer):
    equation = serializers.CharField(max_length=300)
    first = serializers.IntegerField()
    second = serializers.IntegerField()



class DiffSerializer(serializers.Serializer):
    equation = serializers.CharField(max_length=300)
