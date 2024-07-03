from django.shortcuts import render
from .models import Myself, Servises, Portfolio, Contact, Blog
# Create your views here.
def homepageview(request):
    myself = Myself.objects.all()[0]
    servises = Servises.objects.all()
    portfolios = Portfolio.objects.all()
    blog = Blog.objects.all()

    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact.objects.create(
            full_name=name,
            email=email,
            thame=subject,
            message=message
        )
        contact.save()
    return render(request, 'index.html',{'myself':myself, 'servises': servises, 'portfolios':portfolios, 'blogs': blog})

