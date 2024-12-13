# Ex.05 Design a Website for Server Side Processing
## Date: 11-12-2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>Power Calculation (P = I²R)</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style type="text/css">
body {
    background-color:palevioletred;
}
.edge {
    width: 100%;
    padding-top: 250px;
    text-align: center;
}
.box {
    display: inline-block;
    border: thick double rgb(59, 8, 116);
    width: 500px;
    min-height: 300px;
    font-size: 20px;
    background-color: powderblue;
}
.formelt {
    color: black;
    text-align: center;
    margin-top: 7px;
    margin-bottom: 6px;
}
h1 {
    color: black;
    padding-top: 20px;
}
</style>
</head>
<body>
<div class="edge">
    <div class="box">
        <h1>Lamp Filament Power Calculation</h1>
        <form method="POST">
            {% csrf_token %}
            <div class="formelt">
                Current (I): <input type="text" name="current intensity(I in Amps)" value="{{current}}"> A<br/>
            </div>
            <div class="formelt">
                Resistance (R): <input type="text" name="resistance (R in Ohms)" value="{{resistance}}"> Ω<br/>
            </div>
            <div class="formelt">
                <input type="submit" value="Calculate Power"><br/>
            </div>
            <div class="formelt">
                Power (P): <input type="text" name="calculated Power" value="{{power}}"> Watts<br/>
            </div>
        </form>
    </div>
</div>
</body>
</html>

views.html

from django.shortcuts import render

def power(request):
    context = {}
    context['power'] = "0"
    context['current'] = "0"
    context['resistance'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        print('request.POST:', request.POST)
        
        current = request.POST.get('current', '0') 
        resistance = request.POST.get('resistance', '0') 
        print('current(I) =', current)
        print('Resistance(R) =', resistance)
        
        try:
            # Convert inputs to floats for calculation
            current = float(current)
            resistance = float(resistance)
            
            # Power calculation: P = I²R
            power = current ** 2 * resistance
            context['power'] = power
            
        except ValueError:
            # Handle invalid input
            context['error'] = "Please enter valid numeric values for current and resistance."
            context['power'] = "0"
        
        context['current'] = current
        context['resistance'] = resistance
        print('Power(P) =', context['power'])

    return render(request, 'mathapp/math.html', context)

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views  # Updated to match the new app name (mathapp)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('powercalculation/', views.power, name="powercalculation"),  # Updated URL for power calculation
    #path('', views.power, name="powercalculationroot")  # Root URL redirects to power calculation
]

```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-12-11 141844-1.png>)

## HOMEPAGE:

![alt text](<Screenshot 2024-12-11 141844-1.png>)
## RESULT:
The program for performing server side processing is completed successfully.
