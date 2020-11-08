from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editor/', views.editor, name='editor'),
    re_path(r'^(?P<date>\d{4}-\d{2}-\d{2})/$', views.specific, name='specific')
]
