from rest_framework import serializers

from store.models import Store

from .models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer):
    store = serializers.SlugRelatedField(required=True,
                                         slug_field='id',
                                         queryset=Store.objects.all())

    class Meta:
        model = TransactionHistory
        fields = ['id', 'amount_uzs', 'amount_usd',
                  'info', 'store', 'type', 'created', 'updated']
        read_only_fields = ['created', 'updated']

    def validate(self, attrs):
        if not attrs.get('amount_uzs') and not attrs.get('amount_usd'):
            raise serializers.ValidationError(
                'At least one of "amount_uzs" or "amount_usd" is required.')
        return attrs