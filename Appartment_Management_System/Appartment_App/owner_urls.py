
from django.urls import path

from Appartment_App.owner_views import IndexView, Add_Appartment, View_Appartment, View_Images, Single_Apparment_View, \
    View_Booking, View_Services, View_Payment, Feedback, View_Feedback

urlpatterns = [
    path('', IndexView.as_view()),
    path('add_appartment',Add_Appartment.as_view()),
    path('view_appartment',View_Appartment.as_view()),
    path('view_images',View_Images.as_view()),
    path('sinle_appartment_view',Single_Apparment_View.as_view()),
    path('view_booking',View_Booking.as_view()),
    path('services',View_Services.as_view()),
    path('view_payment',View_Payment.as_view()),
    path('feedback',Feedback.as_view()),
    path('View_Feedback',View_Feedback.as_view())


    ]
def urls():
    return urlpatterns, 'owner', 'owner'