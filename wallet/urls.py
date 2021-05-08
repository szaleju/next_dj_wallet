from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('wallet/', WalletDetailView, name='wallet'),
]
