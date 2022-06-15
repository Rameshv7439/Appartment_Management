from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from Appartment_App.models import owner_reg, UserType, user_reg


class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class Owner_Reg(TemplateView):
    template_name = 'owner_reg.html'
    def post(self , request,*args,**kwargs):
        name= request.POST['name']
        address= request.POST['address']
        phone= request.POST['phone']
        email= request.POST['email']
        image=request.FILES['image']
        fi=FileSystemStorage()
        files=fi.save(image.name,image)
        type= request.POST['type']
        location= request.POST['location']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(email=email,username=username):
            print ('pass')
            return render(request,'owner_reg.html',{'message':"already added the username or email"})
        else:
            user = User.objects._create_user(username=username,password=password,email=email,first_name=name,is_staff='1',last_name='0')
            user.save()
            owner=owner_reg()
            owner.user=user
            owner.address= address
            owner.phone= phone
            owner.image= files
            owner.location=location
            owner.type= type
            owner.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "owner"
            usertype.save()
            return render(request, 'index.html', {'message': "successfully added"})



class User_Reg(TemplateView):
    template_name = 'user_reg.html'
    def post(self , request,*args,**kwargs):
        name= request.POST['name']
        address= request.POST['address']
        phone= request.POST['phone']
        email= request.POST['email']
        image=request.FILES['image']
        fi=FileSystemStorage()
        files=fi.save(image.name,image)
        location= request.POST['location']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(email=email,username=username):
            print ('pass')
            return render(request,'owner_reg.html',{'message':"already added the username or email"})
        else:
            user = User.objects._create_user(username=username,password=password,email=email,first_name=name,is_staff='1',last_name='0')
            user.save()
            userr=user_reg()
            userr.user=user
            userr.address= address
            userr.phone= phone
            userr.image= files
            userr.location=location
            userr.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "userr"
            usertype.save()
            return render(request, 'index.html', {'message': "successfully added"})

class Login(TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']

        user = authenticate(username=username,password=password)
        det = User.objects.get(id=1)
        det.last_name=1
        det.save()

        if user is not None:

            login(request,user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "owner":
                    return redirect('/owner')
                # elif UserType.objects.get(user_id=user.id).type == "staff":
                #     return redirect('/staff')
                else:
                    return redirect('/userr')

            else:


                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:

            return render(request,'login.html',{'message':"Invalid Username or Password"})
