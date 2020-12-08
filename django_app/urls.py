from django.conf.urls import url

from django_app import views

urlpatterns = [
    # 增
    url(r'^addStudent', views.add_student),
    # 查所有
    url(r'^getStudents', views.get_students),
    # 查单个
    url(r'^getStudent', views.get_student),
    url(r'^updateStudent', views.update_student),
    url(r'^deleteStudent', views.delete_student),

]