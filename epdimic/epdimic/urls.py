from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from Group07 import dbrequest as g7

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ESS/index', g7.rqst_process),
    path('ESS/situation', g7.rqst_process),
    path('ESS/situation$', g7.rqst_process),
    path('ESS/situation/situationMoreInfo', g7.rqst_process),
    path('ESS/situation/situationMoreInfo$', g7.rqst_process),
    path('ESS/background/Cases', g7.rqst_process),
    path('ESS/background/Cases$', g7.rqst_process),
    url(r'^(?P<path>.*)$', serve, {'document_root': ''}),
]
