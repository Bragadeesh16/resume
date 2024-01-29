from django.shortcuts import render,redirect
from .forms import default_template_form
from .models import default_template

def home(request):
    return render(request,'home.html',{})

def defaultcv(request):
    form = default_template_form
    if request.method == 'POST':
        form = default_template_form(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save()
            pr_key = instance.pk
            request.session['pr_key'] = pr_key
            return redirect('resume')
        else:
            form = default_template()
    return render(request,'defaultcv.html',{'form':form,})

def resume(request):
    pr_key = request.session.get('pr_key', None)
    instance = default_template.objects.get(pk=pr_key)
    return render(request,'resume.html',{'data':instance})

def replace(request):
    form = default_template_form
    pr_key = request.session.get('pr_key', None)
    instance = default_template.objects.get(pk=pr_key)
    if request.method == 'POST':
        form = default_template_form(request.POST,request.FILES)
        if form.is_valid:
            field1_value = request.POST['first_name']
            field2_value = request.POST['last_name']
            field3_value = request.POST['email']
            field4_value = request.POST['phone']
            field5_value = request.POST['address']
            field6_value = request.POST['pin_code']
            field7_value = request.POST['nationality']
            field8_value = request.POST['linkedin']
            instance.first_name,instance.last_name,instance.email,instance.phone,instance.address,instance.pin_code,instance.nationality,instance.linkedin = field1_value,field2_value,field3_value,field4_value,field5_value,field6_value,field7_value,field8_value 
            print(instance.first_name)
            instance.save()
            return redirect('resume')
    return render(request,'replace.html',{'form':form,'instance':instance})