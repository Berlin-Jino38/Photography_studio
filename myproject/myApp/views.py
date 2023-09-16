from django.shortcuts import render,redirect
from .models import *
from .forms import RegisterForm
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    form = RegisterForm()  # Create an empty form instance

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        # You may want to add further logic for form handling in case it's not valid
    return render(request, 'myApp/index.html', {'form': form})


def gallery_view(request):
    data = GalleryModel.objects.all()
    return render(request, 'myApp/gallery.html', {'data': data})

def register_view(request):
    form = RegisterForm()  # Create an empty form instance

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        # You may want to add further logic for form handling in case it's not valid
    return render(request, 'myApp/register.html', {'form': form})

  
def success_view(request):
    return render(request,'myApp/success.html')

def product(request, name):
    if GalleryModel.objects.filter(name=name).exists():
        product = Product.objects.filter(gallery__name=name)
        template = loader.get_template('myApp/gallery_details.html')
        return HttpResponse(template.render({"products": product , "catagory":name}, request))
    else:
        #messages.warning(request, "No such Category found")
        return redirect('category')
    
def aboutus(request):
    return render (request,'myApp/about.html')