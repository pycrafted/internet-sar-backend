from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActualiteViewSet

router = DefaultRouter()
router.register(r'actualites', ActualiteViewSet, basename='actualite')

urlpatterns = [
    path('api/', include(router.urls)),
]


