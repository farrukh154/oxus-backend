from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
import pytz

from .models import BlackListSearch


class BlackListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        name = request.GET.get('name')
        match_percentage = request.GET.get('match_percentage')

        user = request.user

        utc_datetime = datetime.utcnow()
        utc_datetime = utc_datetime.replace(tzinfo=pytz.utc)
        local_datetime = utc_datetime.astimezone(pytz.timezone('Asia/Dushanbe'))
        formatted_datetime = local_datetime.strftime('%Y-%m-%d %H:%M:%S')

        try:
            self.validate_parameters(name, match_percentage)
        except ValidationError as e:
            return JsonResponse({'error': str(e), 'user': str(user), 'current_datetime': formatted_datetime}, status=400)

        try:
            result = BlackListSearch.search_person(name, int(match_percentage))
        except Exception:
            return JsonResponse({'error': 'An unexpected error occurred.', 'user': str(user), 'current_datetime': formatted_datetime}, status=500)

        return JsonResponse({'result': result, 'user': str(user), 'current_datetime': formatted_datetime}, safe=False)

    def validate_parameters(self, name, match_percentage):
        if not name:
            raise ValidationError("Name parameter is required.")
        if not match_percentage:
            raise ValidationError("Match percentage parameter is required.")
        if not match_percentage.isdigit() or not 0 <= int(match_percentage) <= 100:
            raise ValidationError("Match percentage must be an integer between 0 and 100.")
