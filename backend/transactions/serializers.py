from rest_framework import serializers
from .models import *

class TransactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['user', 'amount','uuid','status','created_at']