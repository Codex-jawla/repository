from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'collage',viewset=CollageViewSet)
router.register(r'student',viewset=StudentViewSet)

urlpatterns = [
    path('2211/',include(router.urls)),
    path('',index,name='index')
]
