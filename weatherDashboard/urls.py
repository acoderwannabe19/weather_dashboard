from django.contrib import admin
from django.urls import path
from .views import view_base, view_forecast, view_humidity, view_temperature, view_wind, view_precipitation, view_chart, get_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_base),
    path('forecast/', view_forecast),
    path('temperature/', view_temperature),
    path('humidity/', view_humidity),
    path('precipitation/', view_precipitation),
    path('wind/', view_wind),
    path('chart/', view_chart),
    path('get_data/', get_data, name='get_data'),

]
