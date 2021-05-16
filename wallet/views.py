from django.contrib.auth.models import User
from .models import Wallet, Transaction, Asset
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
    for transaction in transactions:
        print(transaction.asset)
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateTransaction(request):
    user = request.user
    assets = Asset.objects.all()
    data = request.data

    for ass in assets:
        if data['asset'].strip() == str(ass):
            print("ZNALAZLEM", ass)

    if data['asset'] not in assets:
        print('KURWA GON PRZYWIEŹLI')
        asset = Asset.objects.create(
            ticker='nowy',
            name=data['asset'],
        )
        print('ASSET', asset)
    else:
        transaction = Transaction.objects.create(
            user=user,
            asset_id=data['asset'],
            quantity=data['quantity'],
            transaction_type='transfer',
            price=10
        )
    # dodaj przypadek nowego aktywa
    return Response('transaction created')
