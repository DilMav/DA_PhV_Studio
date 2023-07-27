from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')

def blog(request):
    return render(request, 'main/blog.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def pricing(request):
    return render(request, 'main/pricing.html')