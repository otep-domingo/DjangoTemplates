from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name="index"),
    path('myname/',views.name, name="myname"),
    path('bday/', views.birthday, name="bday"),
    path('child/',views.child, name="seechild"),
    path('subjects/',views.subjects, name="subject"),
    path('portfolio/',views.portfolio,name='portfolio'),
]