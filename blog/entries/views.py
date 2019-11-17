from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blog_entries"
    ordering = ['-entry_date']
    paginate_by = 3

class EntryView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html' # we need to create custom .html file for this

class CreateEntryView(CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title','entry_text']

    def form_valid(self,form): # i do not understand this function
        form.instance.entry_author = self.request.user
        return super().form_valid(form)
# Create your views here.
