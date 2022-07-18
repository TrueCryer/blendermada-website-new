from django.urls import path

from .views import MaterialListView, MaterialDetailView, MaterialDownloadView


app_name = 'materials'


urlpatterns = [
    path('', MaterialListView.as_view(), name='index'),
    path('detail/<int:pk>-<slug:slug>/',
         MaterialDetailView.as_view(), name='detail'),
    path('download/<int:pk>-<slug:slug>.blend',
         MaterialDownloadView.as_view(), name='download'),
]
