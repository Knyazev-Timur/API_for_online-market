from django.urls import path

from contacts import views

urlpatterns = [
    path('', views.ContactListView.as_view()),
    path('create/', views.ContactCreateView.as_view()),
    path('<int:pk>/', views.ContactDetailView.as_view()),
    path('<int:pk>/update/', views.ContactUpdateView.as_view()),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view()),
    # path('by_product/', views.ProductManufacturerDetailView.as_view()),
]
