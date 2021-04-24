from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileCreateForm


def home(request):
    if request.method == "POST":
        profile_form = ProfileCreateForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            user_profile = Profile.objects.create(user=request.user,
            knows_math=profile_form.cleaned_data.get("knows_math"),
            knows_singing=profile_form.cleaned_data.get("knows_singing"),
            knows_music=profile_form.cleaned_data.get("knows_music"),
            knows_drawing=profile_form.cleaned_data.get("knows_drawing"),
            knows_video_editing=profile_form.cleaned_data.get("knows_video_editing"),
            knows_animation=profile_form.cleaned_data.get("knows_animation"),
            learn_math=profile_form.cleaned_data.get("learn_math"),
            learn_singing=profile_form.cleaned_data.get("learn_singing"),
            learn_music=profile_form.cleaned_data.get("learn_music"),
            learn_drawing=profile_form.cleaned_data.get("learn_drawing"),
            learn_video_editing=profile_form.cleaned_data.get("learn_video_editing"),
            learn_animation=profile_form.cleaned_data.get("learn_animation"),
            description=profile_form.cleaned_data.get("description"))
        else:
            print("error")
        profiles = Profile.objects.all()
        return redirect("home")
    else:
        profiles = Profile.objects.all()
        form = ProfileCreateForm()
        return render(request, 'home.html', context={
            "profiles": profiles,
            "form": form,
        })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'


# Actual Views:
@login_required
def users_wanting_learn(request):
    return render(request, "wanting_to_learn.html")


@login_required
def users_wanting_to_teach(request):
    return render(request, "wanting_to_teach.html")


@login_required
def fill_out_skills_form(request):
    return render(request, "skills_form.html")

def profile_view(request, user_uuid):
    profile = Profile.objects.get(link=user_uuid)
    user = profile.user
    return render(request, "profile.html", context={
        "profile": profile,
        "profile_user": user,
    })