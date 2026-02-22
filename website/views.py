from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import  Contact
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages

def home(request):
    return render(request, 'website/home.html')

def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'Your ticket failed successfully')
    form = ContactForm()
    return render(request, 'website/Contact.html',{'form':form})

def blog_home(request):
    return render(request, 'website/blog-home.html')

def blog_single(request):
    return render(request, 'website/blog-single.html')
def elements(request):
    return render(request, 'website/elements.html')


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
    form = ContactForm()
    return render(request, 'test.html',{'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
           form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
