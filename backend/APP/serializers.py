from rest_framework import serializers


class NewtonSerializer(serializers.Serializer):
    equation = serializers.CharField(max_length=300)
    first = serializers.IntegerField()
    second = serializers.IntegerField()



class DiffSerializer(serializers.Serializer):
    equation = serializers.CharField(max_length=300)

class TaylorSerializer(serializers.Serializer):
    function = serializers.CharField(max_length=300)
    num_of_iter = serializers.IntegerField()
    center = serializers.IntegerField()