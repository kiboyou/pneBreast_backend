
import uuid

import base64
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ImageSerializer

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

import base64
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ImageSerializer

from .models import Image


class ImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def post(self, request, format=None):
        uploaded_images = self.request.data
        print(len(uploaded_images))

        for image_name, image_file in uploaded_images.items():
            # Process each image file
            format, image_data = image_file.split(';base64,')
            ext = format.split('/')[-1]
            image_file = ContentFile(base64.b64decode(image_data), name='image.{}'.format(ext))

            # Create a dictionary with image file data
            image_data = {'image': image_file}

            #print('image_data image_data image_data:',image_data)
            # Create an instance of the serializer with the image data
            serializer = ImageSerializer(data=image_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
        
        return Response("Images uploaded successfully.", status=200)
    


class ImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    
    

    def post(self, request, format=None):
        uploaded_images = self.request.data

        #uploaded_images = request.data.getlist('uploaded_images')
        #print('self.request.FILES self.request.FILES:',self.request.FILES)
        #uploaded_images = self.request.data.get('uploaded_images', [])
        #print(uploaded_images  )
        #print(len(uploaded_images))

        
        for data_url in uploaded_images:
            # Convert data URL to file
            print('data_url data_url data_url:',data_url)
            format, image_data = data_url.split(';base64,')
            ext = format.split('/')[-1]
            image_file = ContentFile(base64.b64decode(image_data), name='image.{}'.format(ext))

            # Create a dictionary with image file data
            image_data = {'image': image_file}

            # Create an instance of the serializer with the image data
            serializer = ImageSerializer(data=image_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
        
        return Response("Images uploaded successfully.", status=201)




from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializer import ImageSerializer

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    serializer_class = ImageSerializer()


    def post(self, request, format=None):
        uploaded_images = self.request.data['uploaded_images']
        #print(self.request.FILES)
        #uploaded_images=  dict((self.request.FILES).lists()).get('uploaded_images', None) # capturer les images


        #print('uploaded_images uploaded_images: ',uploaded_images)
        for image in uploaded_images:
            #print(image)
            serializer = ImageSerializer(data=image)
            print(serializer)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
'''
