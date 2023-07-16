from django.urls import path

from manufacturer import views

urlpatterns = [
    path('', views.ManufacturerListView.as_view()),
    path('create/', views.ManufacturerCreateView.as_view()),
    path('<int:pk>/', views.ManufacturerDetailView.as_view()),
    path('<int:pk>/update/', views.ManufacturerUpdateView.as_view()),
    path('<int:pk>/delete/', views.ManufacturerDeleteView.as_view()),
    # path('by_product/', views.ProductManufacturerDetailView.as_view()),
]
