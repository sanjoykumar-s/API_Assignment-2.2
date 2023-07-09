from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Dog,Breed
from rest_framework import generics
from .serializer import DogSerializer , BreedSerializer


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'Intro': "Hi! Welcome to the Dog API!",
            'Creator': "This API was created by Sanjoy",
            'Dogs-List': reverse('dog-list', request=request, format=format),
            ##'Dogs-Details': reverse('dog-detail', request=request, format=format),
            'Breeds-List': reverse('breed-list', request=request, format=format),
            ##'Breeds-Details': reverse('breed-detail', request=request, format=format),
        })

class DogList (generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
        
class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
