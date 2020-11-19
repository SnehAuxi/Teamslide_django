# Create your views here.
from django.shortcuts import render
from teamslide.contact import ContactForm,NameForm
from django.template import RequestContext,loader
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import MemberName

@csrf_exempt
def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            num_members = form.cleaned_data['num_members']
            return HttpResponseRedirect(reverse('num_members', 
                       args=(form.cleaned_data['num_members'],)))

    else:
        form = ContactForm()
        return render(request, 'contact/contact.html',{'form':form})

    
@csrf_exempt
def name_members(request, numb):
    if request.method == 'POST':
        numb -= 1
        form = NameForm(request.POST)
        if form.is_valid():
            obj = MemberName() #gets new object
            obj.member_name = form.cleaned_data['name']
            #finally save the object in db
            obj.save()
            return HttpResponseRedirect(reverse('num_members', 
                args=(numb,)))
    else:
        form = NameForm()
        args = {'form':form}
        return render(request, 'num_members.html',args)

@csrf_exempt
def list_members(request):
    if request.method == 'GET':
        member_names = MemberName.objects.all()
        print(member_names)
        return render(request,'members_table.html',locals())