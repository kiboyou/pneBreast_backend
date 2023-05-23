'''
from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('resultatsimageries/', ImageUploadView.as_view(), name='image_upload'),
]
'''

from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('resultatsimageries/', ImageUploadView.as_view(), name='image_upload'),
    path('resultatsimageries/<str:group_id>/', ImageUploadView.as_view(), name='get_group_id'),
]
