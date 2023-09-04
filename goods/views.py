import django_filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from goods.models import RetailNetwork
from goods.serializers import RetailNetworkCreateSerializer, RetailNetworkSerializer, RetailNetworkUpdateSerializer


class RetailNetworkViewSet(ModelViewSet):
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = django_filters.CharFilter(field_name='contact__country')

    def get_serializer_class(self):
        if self.action == 'create':
            return RetailNetworkCreateSerializer
        elif self.action == 'update':
            return RetailNetworkUpdateSerializer
        else:
            return RetailNetworkSerializer
