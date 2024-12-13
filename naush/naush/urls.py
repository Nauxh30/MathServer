from django.contrib import admin
from django.urls import path
from mathapp import views  # Updated to match the new app name (mathapp)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('powercalculation/', views.power, name="powercalculation"),  # Updated URL for power calculation
    #path('', views.power, name="powercalculationroot")  # Root URL redirects to power calculation
]