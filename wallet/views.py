from django.contrib.auth.models import User
from .models import Wallet
from .serializers import UserSerializer, WalletSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def WalletDetailView(request):
    wallet = Wallet.objects.get(user=request.user.id)
    serializer = WalletSerializer(wallet, many=False)
    return Response(serializer.data)
