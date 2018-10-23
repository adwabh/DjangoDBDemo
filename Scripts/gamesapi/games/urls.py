from django.conf.urls import url
from games import views

urlpatterns = [
    url(r'^games/$', views.game_list, name='game_list'),
    url(r'^games/(?P<pk>[0-9]+)/$', views.game_detail, name='game_detail'),
]
