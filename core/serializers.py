# core/serializers.py
from rest_framework import serializers
from .models import Disease

class DiseaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Disease # Tên Model cần tuần tự hóa
    fields = '__all__' # Lấy tất cả các trường (name, cause, is_contagious, treatment)
    # Hoặc fields = ['id', 'name', 'cause'] (nếu chỉ muốn lấy 3 trường)