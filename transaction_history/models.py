from django.db import models


class TransactionHistory(models.Model):
    class Type(models.TextChoices):
        ADDITION = 'ADD', 'Addition'
        SUBTRACTION = 'SUB', 'Subtraction'

    amount_uzs = models.DecimalField(null=True,
                                     blank=True,
                                     max_digits=9,
                                     decimal_places=2)

    amount_usd = models.DecimalField(null=True,
                                     blank=True,
                                     max_digits=9,
                                     decimal_places=2)
    
    info = models.TextField(null=True,
                            blank=True,
                            max_length=1000)

    store = models.ForeignKey('store.Store',
                              on_delete=models.CASCADE,
                              related_name='transaction_histories')

    type = models.CharField(max_length=3,
                            choices=Type.choices,
                            default=Type.ADDITION)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Transaction Histories'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"{self.amount_uzs or self.amount_usd} | store: {self.store.name}"
