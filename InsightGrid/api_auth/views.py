"""
Auth views for admin login and token refresh.
Tokens are extracted from and returned in the response body.
Frontend stores them and sends in Authorization header.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class AdminLoginView(APIView):
    """
    Admin login endpoint.
    Expects: { "email": "...", "password": "..." }
    Returns: { "access": "...", "refresh": "...", "user": { "email": "..." } }
    """
    authentication_classes = []  # No auth required for login
    permission_classes = []  # No permission required for login

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"message": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Django User model uses username, we'll check email as username for admin
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_staff:
            return Response(
                {"message": "Admin access required"},
                status=status.HTTP_403_FORBIDDEN
            )

        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
            }
        }, status=status.HTTP_200_OK)


class AdminTokenRefreshView(TokenRefreshView):
    """
    Token refresh endpoint.
    Expects: { "refresh": "..." } in body.
    Returns: { "access": "..." }
    """
    authentication_classes = []
    permission_classes = []
