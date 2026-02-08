from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contact.html')

def blog_home(request):
    return render(request, 'website/blog-home.html')

def blog_single(request):
    return render(request, 'website/blog-single.html')
def elements(request):
    return render(request, 'website/elements.html')
