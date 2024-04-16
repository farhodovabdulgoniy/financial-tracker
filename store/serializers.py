from rest_framework import serializers

from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()

    class Meta:
        model = Store
        fields = [
            'id',
            'user',
            'name',
            'info',
            'phone_number',
            'location',
            'total_debt_uzs',
            'total_debt_usd',
            'paid_debt_uzs',
            'paid_debt_usd',
            'unpaid_debt_uzs',
            'unpaid_debt_usd',
            'created',
            'updated'
        ]


class StoreUpdateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True,
                                 source='user.username')
    total_debt_uzs = serializers.ReadOnlyField()
    total_debt_usd = serializers.ReadOnlyField()
    paid_debt_uzs = serializers.ReadOnlyField()
    paid_debt_usd = serializers.ReadOnlyField()
    unpaid_debt_uzs = serializers.ReadOnlyField()
    unpaid_debt_usd = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()

    class Meta:
        model = Store
        fields = [
            'id',
            'user',
            'name',
            'info',
            'phone_number',
            'location',
            'total_debt_uzs',
            'total_debt_usd',
            'paid_debt_uzs',
            'paid_debt_usd',
            'unpaid_debt_uzs',
            'unpaid_debt_usd',
            'created',
            'updated'
        ]
