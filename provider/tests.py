
import json
from django.contrib.auth.models import User
from django.contrib.gis.geos import GEOSGeometry
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Providers, ServiceArea


class ClientLogged(APITestCase):

    def setUp(self):
        self.user = User(username='test', is_superuser=True)
        self.user.set_password('test')
        self.user.save()
        self.client.login(username='test', password='test')


class ProviderTests(ClientLogged):

    def test_create_provider(self):

        url = reverse('providers-list')
        data = {
            "name": "Vinay Singh",
            "email": "vxixnxaxy@gmail.com",
            "phone_no": "+917067401728",
            "language": "es",
            "Currency": "USD"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Providers.objects.count(), 1)
        self.assertEqual(Providers.objects.get().name, data['name'])


class ServiceAreaTests(ClientLogged):

    def test_create_servicearea(self):

        url = reverse('servicearea-list')
        data_provider = {
            "name": "Vinay Singh",
            "email": "vxixnxaxy@gmail.com",
            "phone_no": "+917067401728",
            "language": "es",
            "Currency": "USD"
        }
        data = {
            "name": "Cordoba Capital",
            "provider": Providers.objects.create(**data_provider).id,
            "price": "100.00",
            "poly": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [
                                -64.30847167073696,
                                -31.30906179594282
                            ],
                            [
                                -64.05921935143533,
                                -31.30906179594282
                            ],
                            [
                                -64.05647276940445,
                                -31.524117414389952
                            ],
                            [
                                -64.3105316072599,
                                -31.522946786115803
                            ],
                            [
                                -64.30847167073696,
                                -31.30906179594282
                            ]
                        ]
                    ]
                ]
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(ServiceArea.objects.get().name, data['name'])



    def test_check_point_is_inside(self):

        url = reverse('servicearea-list')
        data_provider = {
            "name": "Vinay Singh",
            "email": "vxixnxaxy@gmail.com",
            "phone_no": "+917067401728",
            "language": "es",
            "Currency": "USD"
        }
        mp = {
            "type": "MultiPolygon",
            "coordinates": [
                [
                    [
                        [
                            -77.30847167073696,
                            -28.30906179594282
                        ],
                        [
                            -77.05921935143533,
                            -28.30906179594282
                        ],
                        [
                            -77.05647276940445,
                            -28.524117414389952
                        ],
                        [
                            -77.3105316072599,
                            -28.522946786115803
                        ],
                        [
                            -77.30847167073696,
                            -28.30906179594282
                        ]
                    ]
                ]
            ]
        }

        data_servicearea = {
            "name": "new delhi",
            "provider": Providers.objects.create(**data_provider),
            "price": "100.00",
            "poly": GEOSGeometry(json.dumps(mp))
        }
        point_inside = {
            "type": "Point",
            "coordinates": [-77.187373, -28.3850624]
        }
        sa = ServiceArea.objects.create(**data_servicearea)
        response_in = self.client.get(
            url,
            {'poly__contains': json.dumps(point_inside)},
            format='json'
        )
        self.assertEqual(response_in.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_in.data['features']), 1)


