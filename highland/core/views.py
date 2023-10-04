from django.shortcuts import render
from django.http import HttpResponse
from .models import bottleform
# Create your views here.
def home(request):
    if request.method == 'POST':
          dorm = request.POST.get('dorm')
        campus = request.POST.get('campus')
        bottle_number = request.POST.get('bottleNumber')
        
        # Create a new instance of the BottleForm model and save the data
        bottle_form = BottleForm(dorm=dorm, campus=campus, bottleNumber=bottle_number)
        bottle_form.save()

    return render(request, 'index.html')


def admin(request):
    bottles = bottleform.objects.all()