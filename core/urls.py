import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from dotenv import load_dotenv

load_dotenv()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('account.urls')),
    path('store/', include('store.urls')),
    path('transaction-history/',
         include('transaction_history.urls')),
]

if 'localhost' in os.getenv('ALLOWED_HOSTS'):
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
