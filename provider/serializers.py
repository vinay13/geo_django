from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from provider.models import Providers,ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model=Providers
		fields='__all__'

class ServiceAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model=ServiceArea
        geo_field="poly"
        fields=('name','price','provider')