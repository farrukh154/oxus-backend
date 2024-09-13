import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from division.utils.currency_exchange_updater import currency_exchange_updater

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def synchronize_nbt_currency(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) if request.body else {}
        currency_to = data.get('currencyTo', None)

        currency_exchange_updater(currency_to)
        return Response({'message': 'Синхронизация с НБТ успешно выполнена.'})
    else:
        return Response({'message': 'Неверный метод запроса.'})
