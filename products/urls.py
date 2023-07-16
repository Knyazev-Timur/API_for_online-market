from django.urls import path

from products import views

urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('create/', views.ProductCreateView.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view()),
    # path('by_product/', views.ProductManufacturerDetailView.as_view()),
]
