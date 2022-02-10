#from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [

    path('^datain/$', views.datain, name='datain'),
    path('^dataout/$', views.dataout, name='dataout'),
    path('^checkqr/$', views.checkqr, name='checkqr'),
    path('^query/$', views.query, name='query'),
    path('^test/', views.test),
    path('^login/',views.verify_user),
    path('^builddir/$', views.builddir, name='builddir'),
    # url('^basic/$', views.basci, name='basic'),

]


