

from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = '__all__'



'''
from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = ('image',)  # Make sure to use a tuple or list here
'''