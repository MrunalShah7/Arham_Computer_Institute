from django.urls import path
from . import views
urlpatterns=[
    path("new_adm/",views.NewAddmission.as_view(),name="new_course"),
    path("new_payment/",views.new_payment.as_view(),name="new_payment")

]