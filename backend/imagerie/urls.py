'''
from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('resultatsimageries/', ImageUploadView.as_view(), name='image_upload'),
]
'''

from django.urls import path
from .views import ImageViewSet

urlpatterns = [
    #path('resultatsimageries/post/', ImageViewSet.as_view({'post': 'create'}), name='image_post'),
    path('resultatsimageries/', ImageViewSet.as_view({'get': 'list'}), name='image_upload'),
    path('resultatsimageries/<str:group_id>/', ImageViewSet.as_view({'get': 'retrieve'}), name='get_group_id'),
]
