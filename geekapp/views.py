from django.shortcuts import render, redirect, get_object_or_404
from geekapp.models import Visitor, Host
from django.core.mail import send_mail
from django.contrib import messages
import datetime

def index(request):
    
    if request.method == 'POST':
        host = Host.objects.order_by('-created')
        if host.exists():
            fullname =  request.POST['fullname']
            useremail = request.POST['useremail']
            phonenumber = request.POST['phonenumber']
            records = Visitor.objects.filter(email=useremail)
            if records.exists():
                visitor = records[0]
                if visitor.ischeckedin:
                    messages.warning(request,f'You are already checked in. Please check out in order to check in again.')
                    return redirect('index')
            else:
                visitor = Visitor()
                visitor.email = useremail

            visitor.name = fullname
            visitor.phone = phonenumber
            visitor.checkinrecord()
            visitor.save()

            message = "Hey a visitor just signed into one of our management product \nHis/her details are- \n\nName- {}, \nEmail- {}, \nContact No- {}\nTime during login- {} IST\n\nTeam Innovacer :)".format(fullname, useremail, phonenumber,visitor.checkin)

            Subject = 'New Visitor'
            host = Host.objects.order_by('-created')[0]
            recipients = [host.email]
            sender = 'gautamprateek21@gmail.com'
            send_mail(Subject,message,sender,recipients,fail_silently=False)

            return redirect('submittedform',"_".join(fullname.split(' ')), visitor.pk)
        else:
            messages.warning(request,f'Please enter host information first...')
            return redirect('host')

    return render(request,'geekapp/index.html')

def submittedform(request, name, pk):
    visitor = get_object_or_404(Visitor,pk=pk)
    my_dict = {
        'visitor': visitor
    }
    return render(request,'geekapp/welcome.html', context=my_dict)

def host(request):
    
    if request.method == 'POST':
        fullname =  request.POST['fullname']
        useremail = request.POST['useremail']
        phonenumber = request.POST['phonenumber']

        host = Host()
        host.name = fullname
        host.email = useremail
        host.phone = phonenumber
        host.save()

        return redirect('index')
    return render(request,'geekapp/host.html')

def end(request):
    if request.method == 'POST':
        useremail = request.POST['useremail']
        visitor = Visitor.objects.filter(email=useremail)
        if visitor.exists():
            visitor[0].checkoutrecord()
            host = Host.objects.order_by('-created')[0]
            Subject = 'Innovacer Management'
            recipients = [useremail]
            sender = 'gautamprateek21@gmail.com'
            message = 'Thank you {} for using our service.\n\nWe would like to send you the details of you which we recorded.\n\nName- {}\nPhone- {}\nCheck-in time- {} IST\nCheck-out time- {} IST\nHost- {}\n\nWe are glad that you join us.\nTeam Innovacer :)'.format(visitor[0].name,visitor[0].name,visitor[0].phone,visitor[0].checkin,visitor[0].checkout,host.name)
            send_mail(Subject,message,sender,recipients,fail_silently=False)
            messages.success(request,f'You just checked out, Thanks for using.')
            return redirect('index')
        else:
            messages.warning(request,f'Email address not found! Please enter a valid email address')
    return render(request, 'geekapp/end.html')
