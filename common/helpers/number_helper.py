import json

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponse

def number_to_words_tj(number):
    if number < 0 or number > 999999999:
        raise ValueError("Invalid input: Number must be between 0 and 999999999")

    below_20 = ['сифр', 'як', 'ду', 'се', 'чор', 'панҷ', 'шаш', 'ҳафт', 'ҳашт', 'нӯҳ', 'даҳ', 'ёздаҳ', 'дувоздаҳ',
                'сенздаҳ', 'чордаҳ', 'понздаҳ', 'шонздаҳ', 'ҳабдаҳ', 'ҳаждаҳ', 'нуздаҳ']
    below_100 = ['бист', 'си', 'чил', 'панҷоҳ', 'шаст', 'ҳафтод', 'ҳаштод', 'навад']

    def words_for_number(n):
        if n < 20:
            return below_20[n]
        if n < 100:
            if n % 10 == 0:
                return below_100[(n // 10) - 2]
            else:
                return below_100[(n // 10) - 2] + 'у ' + words_for_number(n % 10)
        if n < 1000:
            if n % 100 == 0:
                return words_for_number(n // 100) + ' сад'
            else:
                return words_for_number(n // 100) + ' саду ' + words_for_number(n % 100)
        if n < 1000000:
            if n % 1000 == 0:
                return words_for_number(n // 1000) + ' ҳазор'
            else:
                return words_for_number(n // 1000) + ' ҳазору ' + words_for_number(n % 1000)

        if n % 1000000 == 0:
            return words_for_number(n // 1000000) + ' миллион'
        else:
            return words_for_number(n // 1000000) + ' миллиону ' + words_for_number(n % 1000000)

    result = words_for_number(number)
    return result.replace('яксад ', 'сад ')

def number_to_words_drob_tj(number):
    number_str = str(number)
    if '.' not in number_str:
        return number_to_words_tj(int(number_str))
    [whole_str, drob_str] = number_str.split('.')
    dahi = len(drob_str)
    whole_part = number_to_words_tj(int(whole_str))
    if int(drob_str) == 0:
        return whole_part
    whole_part_last2 = whole_part[-2:]
    if whole_part_last2 in ('ду', 'се', 'си'):
        whole_part += 'ву'
    else:
        whole_part += 'у'
    if dahi == 1:
        return f'{whole_part} аз даҳ {number_to_words_tj(int(drob_str))}'
    elif dahi == 2:
        return f'{whole_part} аз сад {number_to_words_tj(int(drob_str))}'
    elif dahi == 3:
        return f'{whole_part} аз ҳазор {number_to_words_tj(int(drob_str))}'
    else:
        return f'{whole_part} аз даҳ ҳазор {number_to_words_tj(int(drob_str))}'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def number_to_words_tj_api(request, id):
    return HttpResponse(
        status=HTTP_200_OK,
        content=json.dumps(
            {
                'result': number_to_words_tj(id)
            }
        ),
        content_type="application/json"
    )