from django.urls import path
from . import views

# Đường dẫn: /api/diseases
# Khi truy cập URL này, chạy hàm views.disease_list
urlpatterns = [
    path('desease',views.disease_list, name='disease-list')
]
