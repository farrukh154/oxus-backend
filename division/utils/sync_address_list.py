from django.http import HttpResponse
from rest_framework.status import HTTP_200_OK
import pypyodbc as odbc
from common.abacus.connection import connection_string
from division.models.region import Region
from division.models.town import Town
from division.models.district import District

def sync_address_list(data):

    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT al.* FROM AddressListValue AS al WHERE al.AddressListID = 2') # 2 is for region
    while True:
        row = cursor.fetchone()
        if not row:
            break
        Region.objects.update_or_create(abacus_id = row['addresslistvalueid'], defaults={
            'abacus_id': row['addresslistvalueid'],
            'active': row['active'],
            'name': row['name'],
        })

    cursor.execute('SELECT al.* FROM AddressListValue AS al WHERE al.AddressListID = 3') # 3 is for town
    while True:
        row = cursor.fetchone()
        if not row:
            break
        Town.objects.update_or_create(abacus_id = row['addresslistvalueid'], defaults={
            'abacus_id': row['addresslistvalueid'],
            'active': row['active'],
            'name': row['name'],
            'region': Region.objects.get(abacus_id=row['parentaddresslistvalueid'])
        })

    cursor.execute('SELECT al.* FROM AddressListValue AS al WHERE al.AddressListID = 4') # 4 is for district
    while True:
        row = cursor.fetchone()
        if not row:
            break
        District.objects.update_or_create(abacus_id = row['addresslistvalueid'], defaults={
            'abacus_id': row['addresslistvalueid'],
            'active': row['active'],
            'name': row['name'],
            'town': Town.objects.get(abacus_id=row['parentaddresslistvalueid'])
        })
    return HttpResponse(status=HTTP_200_OK, content='Синхронизация прошла успешно')