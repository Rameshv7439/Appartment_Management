from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

from Appartment_App.models import owner_reg, user_reg, feedback, add_appartment


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class View_Owner(TemplateView):
    template_name = 'admin/view_owner.html'
    def get_context_data(self, **kwargs):
        context = super(View_Owner,self).get_context_data(**kwargs)

        view_owner = owner_reg.objects.filter(user__last_name='0',user__is_staff='1',user__is_active='1')

        context['view_owner'] = view_owner
        return context
class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class Approve_Owner_View(TemplateView):
    template_name = 'admin/owner_approved_view.html'
    def get_context_data(self, **kwargs):
        context = super(Approve_Owner_View,self).get_context_data(**kwargs)

        view_approved_owner = owner_reg.objects.filter(user__last_name='1',user__is_staff='1',user__is_active='1')

        context['view_approved_owner'] = view_approved_owner
        return context

class View_User(TemplateView):
    template_name = 'admin/view_user.html'
    def get_context_data(self, **kwargs):
        context = super(View_User,self).get_context_data(**kwargs)

        view_user = user_reg.objects.filter(user__last_name='0',user__is_staff='1',user__is_active='1')

        context['view_user'] = view_user
        return context

class Approve_User_View(TemplateView):
    template_name = 'admin/user_approved_view.html'
    def get_context_data(self, **kwargs):
        context = super(Approve_User_View,self).get_context_data(**kwargs)

        view_approved_user = owner_reg.objects.filter(user__last_name='1',user__is_staff='1',user__is_active='1')

        context['view_approved_user'] = view_approved_user
        return context

class View_Feedback(TemplateView):
    template_name = 'admin/view_feedback.html'
    def get_context_data(self, **kwargs):
        context = super(View_Feedback,self).get_context_data(**kwargs)

        feedba = feedback.objects.filter(status='added')

        context['feedba'] = feedba
        return context
    def post(self , request,*args,**kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id1 = request.POST['id']
        reply = request.POST['reply']
        rep = feedback.objects.get(id=id1)
        # act.complaint=complaint
        rep.reply= reply
        rep.status = 'replied'
        rep.save()
        return redirect(request.META['HTTP_REFERER'])

class View_Appartment(TemplateView):
    template_name = 'admin/view_appartment.html'
    def get_context_data(self, **kwargs):
        context = super(View_Appartment,self).get_context_data(**kwargs)

        view_appartment = add_appartment.objects.all()

        context['view_appartment'] = view_appartment
        return context

class Single_Apparment_View(TemplateView):
    template_name = 'admin/single_appartment_view.html'
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(Single_Apparment_View,self).get_context_data(**kwargs)

        view_singe_appartment = add_appartment.objects.filter(id=id1)
        context['view_singe_appartment'] = view_singe_appartment
        return context

class View_Images(TemplateView):
    template_name = 'admin/view_images.html'
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(View_Images,self).get_context_data(**kwargs)

        view_image = add_appartment.objects.filter(id=id1)
        context['view_image'] = view_image
        return context