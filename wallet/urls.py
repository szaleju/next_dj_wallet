from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('users/', UserList.as_view(), name='user-list'),
    path('wallet/', WalletDetailView, name='wallet'),
    path('transaction/', CreateTransaction, name='create-transaction'),
    path('transactions/', ListTransactions, name='list-transactions'),
]
