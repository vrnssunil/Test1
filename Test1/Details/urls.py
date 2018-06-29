from django.conf.urls import url,include
from .rest_api import test,getlist,get,post
urlpatterns = [
url(r'^test/',test),
url('list/', getlist),
url(r'^get/(?P<_num>[0-99]+)/',get),
url(r'^post/(?P<_values>[0-99,-]+)/',post)
]
