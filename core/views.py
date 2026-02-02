from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Disease
from .serializers import DiseaseSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def disease_list(request):
  # 1. READ (ORM): Lấy tất cả Object từ DB
  disease = Disease.objects. all()
  
  # 2, SERIALIZE (Tuần tự hóa): Biến đổi Object thành Dictionary
  # many=True vì chúng ta lấy nhiều object
  serializer = DiseaseSerializer(disease, many=True)

  # Kiểm tra nếu request.method bằng POST
  if request.method == 'POST':
    serializer = DiseaseSerializer(data=request.data) #Truyền JSON data nhận được vào Serializer
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data, status=status.HTTP_201_CREATED)