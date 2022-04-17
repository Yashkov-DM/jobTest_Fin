from rest_framework import generics
from car_store.store.models import Store, Car
from car_store.store.serializers import StoreSerializer, CarSerializer


class StoreView(generics.ListAPIView,
                generics.RetrieveAPIView,
                generics.CreateAPIView,
                generics.UpdateAPIView,
                generics.DestroyAPIView,
                generics.GenericAPIView):
    queryset = Store.objects.prefetch_related('cars').all()
    serializer_class = StoreSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class CarView(generics.ListAPIView,
              generics.RetrieveAPIView,
              generics.CreateAPIView,
              generics.UpdateAPIView,
              generics.DestroyAPIView,
              generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.method.upper() == 'GET':

            store_id = self.request.query_params.get('store_id', None)
            if store_id is not None:
                qs = qs.filter(store_id=store_id)

            available = self.request.query_params.get('available', None)
            if available is not None:
                qs = qs.filter(available=int(available))

        return qs

