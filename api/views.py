from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer
from app_name.models import ModelName
from .serializers import ListSerializer

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer

# Complete me
class RestaurantDetailView():
    queryset = ModelName.objects.all()
    serializer_class = ListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


# Complete me
class UpdateView(RetrieveUpdateAPIView):
    queryset = ModelName.objects.all()
    serializer_class = CreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


# Complete me
class DeleteView(DestroyAPIView):
    queryset = ModelName.objects.all()
    serializer_class = ListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'



