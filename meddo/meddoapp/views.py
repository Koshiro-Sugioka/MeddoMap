from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView,ListView,DetailView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from meddoapp.models import Trip, Place, User
from .forms import TripForm, PlaceForm, SignUpForm
from django.conf import settings

def map_view(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'your_template.html', context)


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "meddoapp/home.html"


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = TripForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('meddoapp:detail_trip', kwargs={'pk': self.object.pk})


class TripListView(LoginRequiredMixin, ListView):
    model = Trip
    queryset = Trip.objects.order_by("start_date_time")
    context_object_name = "trip_list"

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)




class TripDetailView(LoginRequiredMixin, DetailView, FormView):
    model = Trip
    context_object_name = "trip"
    form_class = PlaceForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY
        return context

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            return HttpResponseForbidden("You are not allowed to view this page.")
        return obj


class PlaceCreateView(LoginRequiredMixin, CreateView):
    model = Place



class SignUpView(FormView):
    template_name = 'meddoapp/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
