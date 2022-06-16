from rest_framework import generics, viewsets, routers
from .models import Cars
from .serializer import CarsSerializer

class CarsApiViewset(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer



router = routers.DefaultRouter()
router.register(r'cars', CarsApiViewset)
