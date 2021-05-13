from django.contrib.auth.models import User
from .models import Wallet, Transaction
from .serializers import UserSerializer, WalletSerializer, TransactionSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def WalletDetailView(request):
    wallet = Wallet.objects.get(user=request.user.id)
    serializer = WalletSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ListTransactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateTransaction(request):
    user = request.user
    data = request.data
    print("DATA", data)
    transaction = Transaction.objects.create(
        user=user,
        asset_id=3,
        quantity=data['quantity'],
        transaction_type='transfer',
        price=10
    )
    # dodaj przypadek nowego aktywa
    return Response('transaction created')
