from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='index'),
    path('', views.downline_listing, name='downline_listing'),
    path('create_subprofile', views.create_subprofile, name='create_subprofile'),
    path('downline_search', views.downline_search, name='downline_search'),
    path('risk_management', views.risk_management, name='risk_management'),
    path('banking', views.banking, name='banking'),
    path('report_by_player', views.report_by_player, name='report_by_player'),
    path('bet_list', views.bet_list, name='bet_list'),
    path('bet_list_live', views.bet_list_live, name='bet_list_live'),
    path('my_account', views.my_account, name='my_account'),
    path('player_battle', views.player_battle, name='player_battle'),
]
