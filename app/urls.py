from django.conf.urls import url
from app.views import AppFormView

urlpatterns = [
    url(r'^$', AppFormView.as_view(), name='index'),
]