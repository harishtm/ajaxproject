from django.views.generic import CreateView, ListView, UpdateView, DetailView, FormView
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from myapp.forms import *
from django.core import serializers



class StudentListAngularView(ListView):
    template_name = "angular-student-list.html"
    model = Student
    context_object_name = "student_list"


    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset

    def get_context_data(self,**kwargs):
        context = super(StudentListAngularView,self).get_context_data(**kwargs)
        context['request'] = self.request
        context['all_student_list'] = serializers.serialize('json', self.get_queryset())
        print "***********",serializers.serialize('json', self.get_queryset(), fields=('name','age','phone','address'))
        return context

