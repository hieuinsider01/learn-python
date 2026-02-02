# core/serializers.py
from rest_framework import serializers
from .models import Disease, Dealer

class DiseaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Disease # Tên Model cần tuần tự hóa
    fields = '__all__' # Lấy tất cả các trường (name, cause, is_contagious, treatment)
    # Hoặc fields = ['id', 'name', 'cause'] (nếu chỉ muốn lấy 3 trường)

class DealerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dealer
    fields = '__all__'