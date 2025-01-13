from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *
from .models import Collage
from rest_framework.decorators import action

# Create your views here.

# class CollageViewSet(viewsets.ModelViewSet):
#     queryset = Collage.objects.all()
#     serializer_class = CollageSerializer

class CollageViewSet(viewsets.ModelViewSet):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer

    @action(detail=True, methods=['get'])
    def student(self, request, pk):
        try:
            collage = Collage.objects.get(pk=pk)
            emp = Student.objects.filter(collage=collage)
            studentserializer = StudentSerializer(emp, many=True, context={'request': request})
            return Response(studentserializer.data)
        except Exception as e:
            return Response(f'error no data found {e}')



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def index(request):
    return HttpResponse('<h1>Hello Jawla</h1>')