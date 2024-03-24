from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_view, name='home'),
    path('students/', views.students_view, name='students'),
    path('courses/', views.courses_view, name='courses'),
    path('details/<int:student_id>/', views.details_view, name='details'),
]
