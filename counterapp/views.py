from django.shortcuts import render, redirect
from .models import Food,Consume
# Create your views here.
def index(request):
    if request.method=="POST":
        countfood = request.POST['foodconsumed']#posts onoy the object selected in the selection bar
        newfood= Food.objects.get(name = countfood)# get the object name that was selected in the form in the post method
        user = request.user# gives the user who's currently logged in and stores it un user variable
        newfood = Consume(user=user, food_consumed= newfood)
        newfood.save()
        foods= Food.objects.all()
    
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user= request.user)
    return render(request, "index.html", {"foods":foods, "consumed_food":consumed_food})



def delete(request,id):
    deleteconsumed = Consume.objects.get(pk= id)
    if request.method == "POST":
        deleteconsumed.delete()
        return redirect( "index")
        
    else:
        return render(request, "delete.html", {"deletconsumed": deleteconsumed})
        