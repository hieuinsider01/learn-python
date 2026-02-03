from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# 1. Khởi tạo Router
router = DefaultRouter()

# 2. Đăng ký ViewSet (Router sẽ tự tạo /reviews và /review{pk})
router.register(r'reviews', views.ReviewViewSet)
# Đường dẫn: /api/diseases
# Khi truy cập URL này, chạy hàm views.disease_list
urlpatterns = [
    path('diseases/',views.disease_list, name='disease-list'),
    
    #Thêm tất cả các URL do Router tạo ra
    path('', include(router.urls)),
    path('diagnose/', views.diagnose_image, name='diagnose-image')
]