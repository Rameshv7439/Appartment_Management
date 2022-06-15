from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from Appartment_App.models import add_appartment, book_now, owner_reg, service, payment, UserType, feedback


class IndexView(TemplateView):
    template_name = 'owner/owner_index.html'

class Add_Appartment(TemplateView):
    template_name = 'owner/add_appartment.html'
    def post(self , request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        name= request.POST['name']
        contact_details= request.POST['contact_details']
        location= request.POST['location']
        appartment_type= request.POST['appartment_type']
        type = request.POST['type']
        image=request.FILES['image']
        fi=FileSystemStorage()
        files=fi.save(image.name,image)
        image1=request.FILES['image1']
        fi1=FileSystemStorage()
        files1=fi1.save(image1.name,image1)
        image2=request.FILES['image2']
        fi2=FileSystemStorage()
        files2=fi2.save(image2.name,image2)
        image3=request.FILES['image3']
        fi3=FileSystemStorage()
        files3=fi3.save(image3.name,image3)
        image4=request.FILES['image4']
        fi4=FileSystemStorage()
        files4=fi4.save(image4.name,image4)
        rent= request.POST['rent']
        rooms= request.POST['rooms']
        bath_rooms=request.POST['bath_rooms']
        add_appart=add_appartment()
        add_appart.user=user
        add_appart.name= name
        add_appart.contact_details= contact_details
        add_appart.appartment_type=appartment_type
        add_appart.type=type
        add_appart.image= files
        add_appart.image1= files1
        add_appart.image2= files2
        add_appart.image3= files3
        add_appart.image4= files4
        add_appart.location=location
        add_appart.rent=rent
        add_appart.rooms= rooms
        add_appart.bath_rooms= bath_rooms
        add_appart.save()
        return render(request, 'owner/owner_index.html', {'message': "successfully added"})

class View_Appartment(TemplateView):
    template_name = 'owner/view_appartment.html'
    def get_context_data(self, **kwargs):
        context = super(View_Appartment,self).get_context_data(**kwargs)

        view_appartment = add_appartment.objects.filter(user_id=self.request.user.id)

        context['view_appartment'] = view_appartment
        return context

class View_Images(TemplateView):
    template_name = 'owner/view_images.html'
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(View_Images,self).get_context_data(**kwargs)

        view_image = add_appartment.objects.filter(id=id1)
        context['view_image'] = view_image
        return context

class Single_Apparment_View(TemplateView):
    template_name = 'owner/single_appartment_view.html'
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(Single_Apparment_View,self).get_context_data(**kwargs)

        view_singe_appartment = add_appartment.objects.filter(id=id1)
        context['view_singe_appartment'] = view_singe_appartment
        return context

class View_Booking(TemplateView):
    template_name = 'owner/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(View_Booking,self).get_context_data(**kwargs)
        boo= User.objects.get(id=self.request.user.id)
        reg=owner_reg.objects.get(user_id=boo.id)
        print(reg,'qqq')
        view_booking = book_now.objects.filter(owner_id_id=reg.id, status='pending')
        print(view_booking,'qqqqqq')

        context['view_booking'] = view_booking
        return context
    def post(self , request,*args,**kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id1 = request.POST['id']
        print('1111111111111111',id)
        action = request.POST['action']
        rep = book_now.objects.get(id=id1)
        # act.complaint=complaint
        rep.action= action
        rep.status = 'replied'
        rep.save()
        return redirect(request.META['HTTP_REFERER'])

class View_Services(TemplateView):
    template_name = 'owner/view_services.html'
    def get_context_data(self, **kwargs):
        context = super(View_Services,self).get_context_data(**kwargs)
        boo= User.objects.get(id=self.request.user.id)
        app= add_appartment.objects.get(user_id=boo.id)

        view_service = service.objects.filter(appartment_id=app.id)
        context['view_service'] = view_service
        return context
    def post(self , request,*args,**kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id1 = request.POST['id']
        print('1111111111111111',id)
        service_status = request.POST['service_status']
        rep = service.objects.get(id=id1)
        # act.complaint=complaint
        rep.service_status= service_status
        rep.status = 'replied'
        rep.save()
        return redirect(request.META['HTTP_REFERER'])

class View_Payment(TemplateView):
    template_name = 'owner/payment_view.html'
    def get_context_data(self, **kwargs):
        context = super(View_Payment,self).get_context_data(**kwargs)
        boo= User.objects.get(id=self.request.user.id)
        app= add_appartment.objects.get(user_id=boo.id)

        view_payment = payment.objects.filter(appartment_id=app.id)
        context['view_payment'] = view_payment
        return context

class Feedback(TemplateView):
    template_name = 'owner/feedback.html'
    def post(self , request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        type = UserType.objects.get(user_id=self.request.user.id)
        feedb =request.POST['feedback']
        feed = feedback()
        feed.user=user
        feed.type= type
        feed.feedback=feedb
        feed.status='added'
        feed.save()
        return render(request, 'owner/owner_index.html',{'message': "Added"})

class View_Feedback(TemplateView):
    template_name = 'owner/view_feedback.html'
    def get_context_data(self, **kwargs):
        context = super(View_Feedback,self).get_context_data(**kwargs)

        feedba = feedback.objects.filter(user_id=self.request.user.id)

        context['feedba'] = feedba
        return context





