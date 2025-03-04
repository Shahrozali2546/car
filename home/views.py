from django.shortcuts import render, HttpResponse
import joblib
from joblib import load
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, 'static', 'Car_Random_Forest_regressor.pkl')
model = joblib.load(model_path)

#model=joblib.load('static/Car_Random_Forest_regressor')


# Create your views here.

def index(request):
    #return HttpResponse('This is the Home Page')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def prediction(request):
    if request.method == 'POST':
        #print('Enter into the post request')
        name=int(request.POST.get('name'))
        year=int(request.POST.get('year'))
        km_driven=int(request.POST.get('km_driven'))
        fuel=int(request.POST.get('fuel'))
        seller_type=int(request.POST.get('seller_type'))
        transmission=int(request.POST.get('transmission'))
        owner=int(request.POST.get('owner'))
        seats=int(request.POST.get('seats'))
        max_power=int(request.POST.get('max_power'))
        MileageUnit	=int(request.POST.get('MileageUnit'))
        Mileage	=int(request.POST.get('Mileage'))
        Engine=int(request.POST.get('Engine'))

        #print(name,year,km_driven,fuel,seller_type,transmission,owner,seats,max_power,MileageUnit,Mileage,Engine)

        pred = round(model.predict([[name,year,km_driven,fuel,seller_type,transmission,owner,seats,max_power,MileageUnit,Mileage,Engine]])[0])

        #print(pred)

        output={
            'output':pred
        }

        return render(request,'prediction.html',output)
      



    else:
        return render(request,'prediction.html')

