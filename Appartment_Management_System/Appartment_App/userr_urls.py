
from django.urls import path

from Appartment_App.userr_views import IndexView, View_Appartment, Single_Apparment_View, View_Images, Book_Now, \
    View_Booking, Payment, Service, Add_Service, View_Service_Status, Feedback, View_Feedback

urlpatterns = [
    path('', IndexView.as_view()),
    path('view_appartment',View_Appartment.as_view()),
    path('sinle_appartment_view',Single_Apparment_View.as_view()),
    path('view_images',View_Images.as_view()),
    path('book_now',Book_Now.as_view()),
    path('view_booking',View_Booking.as_view()),
    path('payment',Payment.as_view()),
    path('service',Service.as_view()),
    path('add_service',Add_Service.as_view()),
    path('view_service_status',View_Service_Status.as_view()),
    path('feedback',Feedback.as_view()),
    path('View_Feedback',View_Feedback.as_view())


    ]
def urls():
    return urlpatterns, 'userr', 'userr'