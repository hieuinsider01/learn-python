from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Disease, Dealer, Review
from .serializers import DiseaseSerializer, DealerSerializer, ReviewSerializer, ImageUploadSerializer

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
  
class ReviewViewSet(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  
  # LỆNH BẢO MẬT: Chỉ cho phép POST (Create) nếu user đã đăng nhập.
  permission_classes = [IsAuthenticatedOrReadOnly]
  
@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def diagnose_image(request):
  # 1. SERIALIZER: Nhận file ảnh từ request
  serializer = ImageUploadSerializer(data=request.data)
  
  if serializer.is_valid():
    # 2. XỬ LÝ ẢNH (Logic cốt lõi)
    uploaded_image = serializer.validated_data['image']
    
    #TẠM THỜI: Chỉ trả về tên file và kích thước
    response_data = {
      "filename": uploaded_image.name,
      "size_bytes": uploaded_image.size,
      "status": "Image received and validated"
    }
    return Response(response_data, status=status.HTTP_200_OK)
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)