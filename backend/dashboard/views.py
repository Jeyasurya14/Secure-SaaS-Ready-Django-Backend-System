from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from users.permissions import IsAdmin
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .models import APILog
from .serializers import APILogSerializer

User = get_user_model()

class UserStatsView(APIView):
    permission_classes = (IsAdmin,)

    def get(self, request):
        total_users = User.objects.count()
        active_users = User.objects.filter(is_active=True).count()
        new_users_last_30_days = User.objects.filter(date_joined__gte=timezone.now() - timedelta(days=30)).count()

        return Response({
            'total_users': total_users,
            'active_users': active_users,
            'new_users_30d': new_users_last_30_days
        })

class APILogListView(generics.ListAPIView):
    permission_classes = (IsAdmin,)
    queryset = APILog.objects.all().order_by('-timestamp')
    serializer_class = APILogSerializer
