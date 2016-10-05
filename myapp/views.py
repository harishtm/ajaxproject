from django.views.generic import CreateView, ListView, UpdateView, DetailView, FormView, DeleteView
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from myapp.forms import *


class StudentCreateView(CreateView):
    template_name="add-edit-student.html"
    form_class = StudentForm
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['key'] = "add"
        return context


class StudentListView(ListView):
    template_name = "student-list.html"
    model = Student
#    context_object_name = "student_list"

#    def __init__(self, *args, **kwargs):
#        super(StudentListView,self).__init__(*args, **kwargs)

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset

#    def get_context_data(self,**kwargs):
#        context = super(StudentListView,self).get_context_data(**kwargs)
#        context['request'] = self.request
#        return context

    def get(self, request, *args, **kwargs):
        search_text = request.GET.get('search')
        if search_text:
            student_list = Student.objects.filter(name__iexact = request.GET.get('search'))
        else:
            student_list = Student.objects.all()
        return render_to_response("student-list.html",locals())


class StudentEditView(FormView):
    template_name = "add-edit-student.html"
    model = Student
    form_class = StudentForm
    success_url = "/student-list/"

    def get_context_data(self,**kwargs):
        context = super(StudentEditView,self).get_context_data(**kwargs)
        context['key'] = "edit"
        context['stid'] = self.kwargs.get('stid', None)
        return context

#    def get_object(self, queryset=None):
#        """
#            This is for detailview
#        """
#        if queryset is None:
#            queryset = self.get_queryset()
#        pk = self.kwargs.get('stid', None)
#        if pk is not None:
#            queryset = queryset.filter(pk = pk)
#        obj = queryset.get()
#        return obj

    def get_form(self, form_class):
        try:
            obj = Student.objects.get(pk = self.kwargs.get('stid', None))
            return form_class(instance=obj,**self.get_form_kwargs())
        except Student.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_valid(self,form):
        form.save()
        return super(StudentEditView,self).form_valid(form)

class StudentDetailView(DetailView):

    template_name = 'studentdetails.html'
    model = Student
#    queryset = Student.objects.all()
    context_object_name = 'st'

#    def get_queryset(self):
#        queryset = Student.objects.all()
#        return queryset

#    def get_object(self):
#        obj = Student.objects.get(pk = self.kwargs.get('pk'))
#        return obj

class StudentDeleteView(DeleteView):

    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = "/student-list/"

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(StudentDeleteView, self).post(request, *args, **kwargs)














