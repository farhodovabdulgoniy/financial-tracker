from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TransactionHistory


@receiver(post_save, sender=TransactionHistory)
def update_store_debt_on_transaction(sender, instance, created, **kwargs):
    if created:
        store = instance.store
        if instance.type == TransactionHistory.Type.SUBTRACTION:
            store.paid_debt_uzs += instance.amount_uzs or 0
            store.paid_debt_usd += instance.amount_usd or 0

            store.unpaid_debt_uzs -= instance.amount_uzs or 0
            store.unpaid_debt_usd -= instance.amount_usd or 0

        elif instance.type == TransactionHistory.Type.ADDITION:
            store.total_debt_uzs += instance.amount_uzs or 0
            store.total_debt_usd += instance.amount_usd or 0

            store.unpaid_debt_uzs += instance.amount_uzs or 0
            store.unpaid_debt_usd += instance.amount_usd or 0            
        store.save()