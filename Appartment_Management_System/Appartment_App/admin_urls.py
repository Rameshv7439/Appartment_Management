
from django.urls import path

from Appartment_App.admin_views import IndexView, View_Owner, ApproveView, RejectView, Approve_Owner_View, View_User, \
    Approve_User_View, View_Feedback, View_Appartment, Single_Apparment_View, View_Images

urlpatterns = [
    path('', IndexView.as_view()),
    path('view_owner',View_Owner.as_view()),
    path('approve',ApproveView.as_view()),
    path('remove',RejectView.as_view()),
    path('approved_owner',Approve_Owner_View.as_view()),
    path('view_user',View_User.as_view()),
    path('approved_user',Approve_User_View.as_view()),
    path('view_feedback',View_Feedback.as_view()),
    path('view_appartment',View_Appartment.as_view()),
    path('sinle_appartment_view',Single_Apparment_View.as_view()),
    path('view_images',View_Images.as_view())

    ]
def urls():
    return urlpatterns, 'admin', 'admin'