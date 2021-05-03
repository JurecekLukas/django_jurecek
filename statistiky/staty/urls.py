from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.StatsListView.as_view(), name='list'),
    path('detail/<int:pk>', views.StatsDetailView.as_view(), name='detail'),
]