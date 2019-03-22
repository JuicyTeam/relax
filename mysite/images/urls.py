from django.conf.urls import url
from images.views import imageclass

urlpatterns = [
    #url(r'^model', test),
    url(r'^class$', imageclass)
]
