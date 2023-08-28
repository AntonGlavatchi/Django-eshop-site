from django.urls import path

from . import views


app_name = 'productsmodule'
urlpatterns = [
	path('index/', views.index_view, name='index_view'),
]