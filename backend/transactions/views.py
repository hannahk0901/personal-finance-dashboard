from django.http import JsonResponse
from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer

def ping(request):
    return JsonResponse({"ok": True})

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer
