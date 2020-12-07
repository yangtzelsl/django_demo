import random

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 自定义view
from django_app.models import Student


def hello(request):
    """
    视图函数
    :param request: 请求的地址
    :return:
    """
    return HttpResponse("hello django!~~~~~~~~~~~~~~~~")


def index(request):
    return render(request, 'index.html')


def add_student(request):

    student = Student()
    student.s_name = 'tom %s'%random.randrange(100)

    # 保存DB
    student.save()

    # 普通的字符串返回，使用 HttpResponse 即可
    return HttpResponse("student add success")


def get_students(request):

    # 获取所有
    students = Student.objects.all()

    for student in students:
        print(student.s_name)

    # 拿到后放到字典中返回给前端
    context = {
        "students":students,
    }

    # 如果要加载页面，就需要使用 render 渲染
    # 将获取的context直接返回
    return render(request,"student_list.html",context=context)