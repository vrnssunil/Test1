from django.conf.urls import url,include
from .rest_api import test,getlist,post
urlpatterns = [
url(r'^test/',test),
url('list/', getlist),
rl(r'^post/',add_cal)

]
