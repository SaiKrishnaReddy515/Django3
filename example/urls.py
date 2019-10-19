from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns=[

  #  path('',views.index,name="index"),
   # path('add',views.add,name="add"),
 #   path('test',views.test,name="test"),
   # path('std',views.std,name="std")
   url(r'^$',views.index,name='index'),
   url(r'^add$',views.add,name="add"),
    url(r'^test2$',views.test2,name="test2"),
    url(r'^DB1$',views.DB1,name='DB1'),
    url(r'^std$',views.std,name='std')
   



]