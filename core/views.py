from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Disease, Dealer
from .serializers import DiseaseSerializer, DealerSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def disease_list(request):
  # --- 1. LOGIC POST (Tạo mới) ---
  if request.method == 'POST':
    # Nhận dữ liệu JSON từ requesst và truyền vào Serializer
    serializer = DiseaseSerializer(data=request.data)
    
    # Kiểm tra tính hợp lệ
    if serializer.is_valid():
      serializer.save() # Lưu vào Database (Sử dụng ORM)
      # Trả về kết quả JSON đã tạo và mã 201 (Created)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Trả về mã 400 (Bad Request) nếu dữ liệu không hợp lệ
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  # --- 2. LOGIC GET (Đọc danh sách) --- 
  # Logic này chỉ chạy khi request.method là GET
  if request.method == 'GET':
    diseases = Disease.objects.all() # ORM: Lấy tất cả Object
    serializer = DiseaseSerializer(diseases, many=True) # Tuần tự hóa List Object
    return Response(serializer.data)

#Class này xử lý GET (List) và POST (Create)
class DealerListCreateView(generics.ListCreateAPIView):
  queryset = Dealer.objects.all() # ORM: Định nghĩa dữ liệu gốc
  serializer_class = DealerSerializer