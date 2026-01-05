from django.urls import path
from .views import UserStatsView, APILogListView

urlpatterns = [
    path('stats/users/', UserStatsView.as_view(), name='user_stats'),
    path('logs/api/', APILogListView.as_view(), name='api_logs'),
]
