
from django.conf.urls import url
from django.contrib import admin

from users.views import IndexView

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', IndexView.as_view(), name='index'),
]
