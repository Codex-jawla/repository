from rest_framework import serializers
from .models import *

# class CollageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Collage,
#         fields = '__all__'

class CollageSerializer(serializers.HyperlinkedModelSerializer):
    collage_id=serializers.ReadOnlyField()
    class Meta:
        model = Collage
        fields = '__all__'

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    student_id=serializers.ReadOnlyField()
    class Meta:
        model = Student
        fields = '__all__'