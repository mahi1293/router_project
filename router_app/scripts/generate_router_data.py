import csv
import os

from django.conf import settings
from router_api.models import Router

csv_path = os.path.join(settings.BASE_DIR, 'scripts/router_data.csv')


def create():
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            count += 1
            router, created = Router.objects.get_or_create(sapid=row['Sap Id'])
            router.hostname = row['Host Name']
            router.loopback = row['Loop Back']
            router.mac_address = row['Mac Address']
            router.save()
            print("count: %s \r" % count, end=' ')
    return True
