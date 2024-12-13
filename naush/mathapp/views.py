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
