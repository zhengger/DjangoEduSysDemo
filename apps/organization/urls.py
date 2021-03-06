#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/5/21 0021. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways

from organization.views import OrgView, AddUserAskView, AddFavView

from django.urls import path, re_path
from .views import OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, TeacherListView, TeacherDetailView

# 命名空间
app_name = "organization"

urlpatterns = [
    # 机构列表
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
    # 机构首页，课程，介绍，教师
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),
    re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name="org_course"),
    re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name="org_desc"),
    re_path('teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name="org_teacher"),
    # 收藏机构
    path('add_fav/', AddFavView.as_view(), name="add_fav"),
    # 讲师列表
    path('teacher/list/', TeacherListView.as_view(), name="teacher_list"),
    # 讲师详情
    re_path('teacher/detail/(?P<teacher_id>\d+)/', TeacherDetailView.as_view(), name="teacher_detail"),

]
