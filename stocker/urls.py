from django.urls import path
from. import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"), 
    path('stockpage', views.stockpage, name="stockpage"),
    path('delete/<stock_id>', views.delete, name='delete'),
]
