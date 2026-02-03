# core/serializers.py
from rest_framework import serializers
from .models import Disease, Dealer, Review

class DiseaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Disease # Tên Model cần tuần tự hóa
    fields = '__all__' # Lấy tất cả các trường (name, cause, is_contagious, treatment)
    # Hoặc fields = ['id', 'name', 'cause'] (nếu chỉ muốn lấy 3 trường)

class DealerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dealer
    fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
  # Thêm trường chỉ đọc (read_only) để hiển thị tên Dealer thay vì ID
  dealer_name = serializers.ReadOnlyField(source='dealer.name')
  
  class Meta:
    model = Review
    # Thêm 'dealer_name' vào fields để hiển thị
    fields = ['id', 'dealer', 'rating', 'comment', 'created_at']
    # Thêm 'read_only_fields' để ngăn User gửi dữ liệu vào các trường này
    read_only_fields = ['created_at']
    
# Serializer để nhận file
class ImageUploadSerializer(serializers.Serializer): # KHÔNG DÙNG ModelSerializer
  image = serializers.ImageField() # Field chuẩn để nhận ảnh