from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('account.urls')),
    path('store/', include('store.urls')),
    path('transaction-history/',
         include('transaction_history.urls')),
]