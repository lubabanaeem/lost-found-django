
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

def home(request):

    # CREATE (form submit) inserting new row in database
    if request.method == "POST":
        Item.objects.create(
            type=request.POST['type'],
            category=request.POST['category'],
            name=request.POST['name'],
            location=request.POST['location'],
            date=request.POST['date'],
            contact=request.POST['contact']
        )
        return redirect('home')

    # READ (search + listing)
    query = request.GET.get('q')
    if query:
        items = Item.objects.filter(name__icontains=query) | Item.objects.filter(category__icontains=query)
    else:
        items = Item.objects.all()

    return render(request, 'home.html', {'items': items})

