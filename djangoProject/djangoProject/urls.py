from django.contrib import admin
from django.urls import path
from NewProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_form/', views.student_create, name='student_view'),
    path('student_detail/', views.student_retrieve, name='student_detail'),
    path('student_detail/<int:pk>', views.student_retrieve_id, name='student_detail_id'),
    path('student_update/<int:pk>', views.student_update, name='student_update'),
    path('student_delete/<int:pk>', views.student_delete, name='student_update'),

]
