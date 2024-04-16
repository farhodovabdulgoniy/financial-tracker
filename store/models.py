from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    info = models.TextField(null=True,
                            blank=True,
                            max_length=1000)
    phone_number = models.CharField(null=True,
                                    blank=True,
                                    max_length=20)
    location = models.CharField(null=True,
                                blank=True,
                                max_length=255)
    
    total_debt_uzs = models.DecimalField(null=True,
                                         blank=True,
                                         max_digits=12,
                                         decimal_places=2)
    total_debt_usd = models.DecimalField(null=True,
                                         blank=True,
                                         max_digits=12,
                                         decimal_places=2)
    
    paid_debt_uzs = models.DecimalField(null=True,
                                        blank=True,
                                        max_digits=12,
                                        decimal_places=2)
    paid_debt_usd = models.DecimalField(null=True,
                                        blank=True,
                                        max_digits=12,
                                        decimal_places=2)
    
    unpaid_debt_uzs = models.DecimalField(null=True,
                                        blank=True,
                                        max_digits=12,
                                        decimal_places=2)
    unpaid_debt_usd = models.DecimalField(null=True,
                                        blank=True,
                                        max_digits=12,
                                        decimal_places=2)

    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             related_name='stores',
                             on_delete=models.SET_NULL)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"{self.name} | owner: {self.user.username}"
