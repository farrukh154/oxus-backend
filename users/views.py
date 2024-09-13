from django.shortcuts import render


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if old_password and new_password:
            user = request.user
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user) 
                return Response({'message': 'Пароль успешно изменен.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Неправильный старый пароль.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Требуется как старый пароль, так и новый пароль.'}, status=status.HTTP_400_BAD_REQUEST)