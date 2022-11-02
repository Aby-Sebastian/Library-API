from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'^Book', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('library/', BookAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls'))    
]

# urlpatterns = format_suffix_patterns(urlpatterns)