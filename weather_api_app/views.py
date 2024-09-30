from .serializers import CItySerializer
from .models import City
import requests
from rest_framework import status
from django.http import HttpResponse, JsonResponse

# Create your views here.
def weather_api(request, city):
    api_key = '45fca6311faBa41b61aee922ec47c231'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q':city,
        'appid':api_key,
        'units':'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        city_obj = City.objects.create(name=city, temperature=temperature, humidity=humidity, description=description)

        serializer = CItySerializer(city_obj)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse('Unable to fetch data', status=status.HTTP_400_BAD_REQUEST)