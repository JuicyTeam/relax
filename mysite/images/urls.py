from django.conf.urls import url
from images.views import Imageclass

urlpatterns = [
    #url(r'^model', test),
        url(r'^class$', Imageclass.as_view())
]
