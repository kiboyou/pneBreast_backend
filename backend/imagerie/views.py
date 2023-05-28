
import uuid
import base64

from rest_framework import viewsets
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .serializer import ImageSerializer
from .models import Image

class ImageViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def create(self, request):
        uploaded_images = self.request.data
        print(len(uploaded_images))

        group_id = uuid.uuid4()  # Generate a new UUID for the group of images

        for image_name, image_file in uploaded_images.items():
            # Process each image file
            format, image_data = image_file.split(';base64,')
            ext = format.split('/')[-1]
            image_file = ContentFile(base64.b64decode(image_data), name='image.{}'.format(ext))

            unique_id = uuid.uuid4().hex  # Generate a unique ID for each image

            # Create a dictionary with image file data, group_id, and unique_id
            image_data = {'group_id': group_id, 'unique_id': unique_id, 'image': image_file}
            print(image_data)

            serializer = ImageSerializer(data=image_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
        
        return Response("Images uploaded successfully.", status=200)
        
    def list(self, request):
        images = Image.objects.values('group_id').distinct()
        serializer = ImageSerializer(images, many=True)
        data = serializer.data
        
        return Response(data)
        
    def retrieve(self, request, group_id=None):  # Update the parameter name to group_id
        images = Image.objects.filter(group_id=group_id)  # Update the filter parameter
        serializer = ImageSerializer(images, many=True)
        data = serializer.data
        print('data data data:',data)

        return Response(data)

'''
import base64
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ImageSerializer
from rest_framework.decorators import action


from .models import Image

class ImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    
    def post(self, request, format=None):
        uploaded_images = self.request.data
        print(len(uploaded_images))

        group_id = uuid.uuid4()  # Generate a new UUID for the group of images

        for image_name, image_file in uploaded_images.items():
            # Process each image file
            format, image_data = image_file.split(';base64,')
            ext = format.split('/')[-1]
            image_file = ContentFile(base64.b64decode(image_data), name='image.{}'.format(ext))

            unique_id = uuid.uuid4().hex  # Generate a unique ID for each image

            # Create a dictionary with image file data, group_id, and unique_id
            image_data = {'group_id': group_id, 'unique_id': unique_id, 'image': image_file}
            print(image_data)

            serializer = ImageSerializer(data=image_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
        
        return Response("Images uploaded successfully.", status=200)
    
 
    def get(self, request, format=None):
        images = Image.objects.values('group_id').distinct()
        serializer = ImageSerializer(images, many=True)
        data = serializer.data
        
        return Response(data)


    def get_group_id(self, request, group_id, format=None):
        images = Image.objects.filter(group_id=group_id)
        serializer = ImageSerializer(images, many=True)
        data = serializer.data

        return Response(data)

'''
