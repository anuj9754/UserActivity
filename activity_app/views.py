from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from activity_app.models import User, ActivityPeriod


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):

    activity_periods = ActivitySerializer(source='activity_map', many=True)

    class Meta:
        model = User
        fields = ["id", "real_name", "tz", "activity_periods"]


class UserActivity(APIView):

    def get(self, request):
        queryset = User.objects.all()

        serializer = UserSerializer(queryset, many=True).data
        return Response({"Ok": True, "members": serializer})
