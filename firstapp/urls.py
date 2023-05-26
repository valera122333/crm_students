from django.urls import path
from firstapp import views
urlpatterns = [
path("", views.home, name="home"),
path("groups/", views.user_groups, name="user_groups"),
path("add_group/", views.add_group, name="add_group"),
path("add_students/", views.add_students, name="add_students"),
path("students_list/", views.user_students_list, name="user_students_list"),
path("group_detail/<int:group_id>", views.group_detail, name="group_detail"),
path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
path('export-students/', views.export_students_to_excel, name='export_students'),
path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
path('filter/', views.filter_students, name='filter_students'),

path('group/edit/<int:group_id>/', views.edit_group, name='edit_group'),
path('group/<int:group_id>/delete/', views.delete_group, name='delete_group'),
path('profile/', views.edit_profile, name='edit_profile'),

#Админка
 path('users_list/', views.user_list, name='user_list'),
 path('export_teachers_to_excel/', views.export_teachers_to_excel, name='export_teachers_to_excel'), 
path('teacher/<int:teacher_id>/group/<int:group_id>/', views.teacher_group, name='teacher_group'),
 
  
 
]