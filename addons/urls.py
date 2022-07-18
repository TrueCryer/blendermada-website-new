from django.urls import path

from .views import AddOnActualView, AddOnArchiveView


app_name = 'addons'


urlpatterns = [
    path('', AddOnActualView.as_view(), name='actual'),
    path('archive/', AddOnArchiveView.as_view(), name='archive'),
]
