from rest_framework import serializers

class HelloSerializer(serializers.Serializer): #class HelloSerializer(BaseClass.Serializer(class_name))
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
