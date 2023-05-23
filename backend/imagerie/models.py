import uuid
from django.db import models

class Image(models.Model):
    group_id = models.UUIDField(default=uuid.uuid4)
    unique_id = models.CharField(max_length=100, unique=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.unique_id


'''
import uuid
from django.db import models

class Image(models.Model):
    
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image)

'''