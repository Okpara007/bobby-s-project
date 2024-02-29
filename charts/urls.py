# collect from listings urls.py p.s we are setting up the routes for the accounts app

from django.urls import path
from .views import ChartChartView, AdminLoginView
from . import views 

urlpatterns = [
    path('admin-login/', AdminLoginView.as_view(), name='admin_login'),
    path('', ChartChartView.as_view(), name="charts"), # first parameter(root path/home page), second parameter(mathod that we want to connect it to), final parameter(the name which would be used to easily access the path)
    path('pie/', views.pie_chart, name='pie_chart'),
    path('line/', views.line_chart, name='line_chart'),
    path('doughnut/', views.doughnut_chart, name='doughnut_chart'),
    path('polar/', views.polar_area_chart, name='polar_area_chart'),
]