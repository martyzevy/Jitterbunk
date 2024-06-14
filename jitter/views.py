from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import User, Bunk
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from .forms import bunkSomeoneForm

class BunkView(generic.ListView):
    template_name = 'jitter/index.html'
    context_object_name = 'list_of_bunks'
    def get_queryset(self):
        return Bunk.objects.filter(
        time__lte=timezone.now()
    ).order_by('time')

class IndividualsView(generic.DetailView):
    model = User
    template_name = 'jitter/individuals.html'

def get_bunking_users(request):
    if request.method == "POST":
        form = bunkSomeoneForm(request.POST)
        if form.is_valid():
            fUser = form.cleaned_data['fromUser']
            tUser = form.cleaned_data['toUser']
            newBunk = Bunk(fromU=fUser, toU=tUser, time=timezone.now())
            newBunk.save()
            fUser.bunks.add(newBunk)
            tUser.bunks.add(newBunk)
    else:
        form = bunkSomeoneForm()
    return render(request, 'jitter/bunk.html', {'form': form})
        
