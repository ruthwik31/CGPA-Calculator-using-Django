from django.urls import path
from .views import *

urlpatterns = [
    path('', cal_cgpa, name='cal_cgpa'),
    path('edit/<int:subject_id>/', subj_edit, name='subj_edit'),
    path('delete/<int:subject_id>/', subj_delete, name='subj_delete'),
    path('result/', result, name='result'),
    path('login/' , login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', custom_logout, name="logout"),
]
