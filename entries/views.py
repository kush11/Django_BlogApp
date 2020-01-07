from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry
# Create your views here.

class HomeView(LoginRequiredMixin,ListView):
    model = Entry
    template_name = 'index.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 3

class EntryView(LoginRequiredMixin,DetailView):
    model= Entry
    template_name = 'entry-detail.html'

class CreateEntityView(LoginRequiredMixin,CreateView):
    model = Entry
    template_name = 'create-view.html'
    fields=['entry_title','entry_text']
    
    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)

def Blog(request):
    entries_list = Entry.objects.all() 
    return render(request,'index.html',{'entries_list':entries_list})

def DetailView(request):
    entries_list = Entry.objects.all() 
    return render(request,'entry-detail.html',{'entries_list':entries_list})
