from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import Meetup, Participant
from .forms import RegistrationForm


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetings/index.html',
                  {'meetups': meetups})


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_from = RegistrationForm()
            return render(request, 'meetings/meetup-details.html',
                          {'meetup_found': True, 'meetup': selected_meetup, 'form': registration_from})
        else:
            registration_from = RegistrationForm(request.POST)
            if registration_from.is_valid():
                user_email = registration_from.cleaned_data['email']
                participant, was_created = Participant.objects.get_or_create(
                    email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')
        return render(request, 'meetings/meetup-details.html',
                      {'meetup_found': True, 'meetup': selected_meetup, 'form': registration_from})

    except Exception as exc:
        print(exc)
        return render(request, 'meetings/meetup-details.html',
                      {'meetup_found': False})


def confirm_registration(request):
    return render(request, 'meetings/registration-success.html')
