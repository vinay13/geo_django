from django.conf.urls import include,patterns,url
from provider import views
from provider.views import ProviderViewSet,ServiceAreaViewSet
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register(r'providers',ProviderViewSet)
router.register(r'servicearea',ServiceAreaViewSet)

urlpatterns=patterns('',
    url(r'',include(router.urls)),


)