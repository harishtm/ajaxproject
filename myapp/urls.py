from django.conf.urls import patterns, include, url
from myapp.views import StudentCreateView,StudentListView, StudentEditView, StudentDetailView, StudentDeleteView
from myapp.forms import *
from django.views.generic import ListView, DetailView
from myapp.angular_view import StudentListAngularView


urlpatterns = patterns('',

    url(r'^add-student/$', StudentCreateView.as_view(), name="student_create_view"),
    url(r'^student-list/$', StudentListView.as_view(), name="student_list_view"),
    url(r'edit-student/(?P<stid>.*)/$', StudentEditView.as_view(), name="student_edit_view"),
    url(r'^student-detail/(?P<pk>.*)/$',StudentDetailView.as_view(), name="student_detail_view"),
    url(r'^delete-student/(?P<pk>.*)/$',StudentDeleteView.as_view(), name="student_delete"),

)

urlpatterns += patterns('',

    url(r'^student-list-angular/$', StudentListAngularView.as_view(), name="student_list_angular_view"),

)
