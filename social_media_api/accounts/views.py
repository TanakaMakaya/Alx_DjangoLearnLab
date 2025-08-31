from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    generics.GenericAPIView

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=400)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=200)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        if request.user == user_to_unfollow:
            return Response({"error": "You cannot unfollow yourself."}, status=400)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=200)


class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following.all()

