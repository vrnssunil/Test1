from django.conf.urls import url,include
from .rest_api import test,getlist,add_cal,post,apinum
urlpatterns = [
url(r'^test/',test),
url('list/', getlist),
url(r'^post/',add_cal),
url(r'^postnum/(?P<_number>[0-99]+)',post),
url(r'^apinum/(?P<_number>[0-99]+)',apinum)


]
