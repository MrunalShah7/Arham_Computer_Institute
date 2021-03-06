from django.urls import path
from . import views
urlpatterns=[
    path("new/",views.NewCourse.as_view(),name="new_course"),
    path("view/",views.ViewCourse.as_view(),name="courses_list"),
    path("update/<int:pk>/",views.updatecourse.as_view(),name="courses_update"),
    path("delete/<int:pk>",views.deletecourse.as_view(),name="courses_delete")
]