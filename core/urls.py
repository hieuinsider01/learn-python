from django.urls import path
from . import views

# Đường dẫn: /api/diseases
# Khi truy cập URL này, chạy hàm views.disease_list
urlpatterns = [
    path('diseases/',views.disease_list, name='disease-list'),
    path('dealers/',views.DealerListCreateView.as_view(), name='dealer-list-create')
]
