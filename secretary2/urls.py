from django.conf.urls import url
from django.contrib import admin
from web import views

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^diary/$', views.diary),
        url(r'^diary/add/$', views.diary_add),
        url(r'^$',views.diary),
]