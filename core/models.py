from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
# Class này sẽ trở thành BẢNG 'core_disease' trong Database
class Disease(models.Model):
  # Field 1: Tên bệnh (String ngắn)
  # CharField là kiểu dữ liệu cho chuỗi có giới hạn độ dài
  name = models.CharField(max_length=100, unique=True)
  
  # Field 2: Nguyên nhân (String dài hơn)
  # TextField là kiểu dữ liệu cho chuỗi dài, không giới hạn
  cause = models.TextField()
  
  # Field 3: Khả năng lây lan
  #BooleanField là kiểu dữ liệu True/False
  is_contagious = models.BooleanField(default=False)
  
  # Field 4: Phương pháp điều trị
  # Vì đây là một List (nhiều thuốc), trong DB thường được lưu là chuỗi dài
  # (hoặc liên kết với bảng khác - sẽ học sau). Tạm thời dùng TextField.
  suggestted_treatment = models.TextField()
  
  # Hàm __str__ (Tương đương get_display_info cho Admin)
  # Hàm này định nghĩ cách hiển thị Object khi được in ra
  def __str__(self):
    return self.name

class Dealer(models.Model):
  name = models.CharField(max_length=100)
  address = models.TextField()
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Review(models.Model):
  dealer = models.ForeignKey('Dealer', on_delete=models.CASCADE)
  rating = models.IntegerField(
    validators=[
      MinValueValidator(1),
      MaxValueValidator(5)     
    ]
  )
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)