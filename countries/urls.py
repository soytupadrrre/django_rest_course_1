from django.urls import path
from countries import views

urlpatterns = [
    path('countries', views.countries_list),
    path('countries/<int:pk>', views.countries_detail)
]
