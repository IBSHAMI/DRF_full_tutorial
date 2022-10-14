from rest_framework import serializers


class UserProductSerializer(serializers.Serializer):
    # We declare what data we want to return
    # We can also return the whole model
    username = serializers.CharField(read_only=True)
