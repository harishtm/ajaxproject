from django.views.generic import CreateView
from django.shortcuts import render

class StudentCreateView(CreateView):

    success_url = "/add-student/"

    def __init__(self, *args, **kwargs):
        super(StudentCreateView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView,self).get_context_data(**kwargs)
        context['request'] = self.request
        return context
