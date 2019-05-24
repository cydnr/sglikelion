from django.conf.urls import url
from django.contrib import admin
import wordcount.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', wordcount.views.home, name="home"),
    url(r'about', wordcount.views.about, name="about"),
    url(r'result', wordcount.views.result, name="result"),
]
