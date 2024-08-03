from django.shortcuts import render
from app.models import Name
from app.forms import Form
from django.http import HttpResponseRedirect

# Create your views here.

def view(request):
    query = Name.objects.all().order_by('-id')

    form = Form(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = Form()

    dec = {'query': query, 'form': form}


    return render(request, 'index.html', dec)