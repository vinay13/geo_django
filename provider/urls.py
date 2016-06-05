from django.conf.urls import include,patterns,url
from provider import views
from provider.views import ProviderViewSet,ServiceAreaViewSet
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register(r'providers',ProviderViewSet)
router.register(r'servicearea',ServiceAreaViewSet)

urlpatterns=patterns('',
    url(r'',include(router.urls)),
    url(r'^search_areas/(?P<lat>(\-?\d+(\.\d+)?))/(?P<lon>(\-?\d+(\.\d+)?))/$',
        views.SearchAreas.as_view(), name='search_areas'),


)
