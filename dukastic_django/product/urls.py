from django.urls import path,include
from product import views

urlpatterns = [
    path('latest_products/', views.LatestProductsList.as_view(),name="latest_products"),
    path('products/search/',views.search,name='search'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(),name="latest_products"),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
