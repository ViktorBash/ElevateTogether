from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileCreateForm, ProfileEditForm


# Homepage with landing page, form to create a profile, and place to view everybody
def learn(request):
    """
    The homepage has a profile form that must be completed to see the profiles of other members
    """
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
        return redirect("learn")
    else:
        profiles = Profile.objects.all()
        form = ProfileCreateForm()
        return render(request, 'learn.html', context={
            "profiles": profiles,
            "form": form,
        })


# Create an account (User model)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


# See the profile of someone (uses UUID to create a custom URL)
@login_required
def profile_view(request, user_uuid):
    profile = Profile.objects.get(link=user_uuid)
    return render(request, "profile.html", context={
        "profile": profile,
    })


# Update your own profile (similar mechanics to the create profile form/view)
@login_required
def profile_update(request):
    if request.method == "POST":
        profile_form = ProfileEditForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            user_profile = Profile.objects.get(user=request.user)
            user_profile.knows_math = profile_form.cleaned_data.get("knows_math")
            user_profile.knows_singing = profile_form.cleaned_data.get("knows_singing")
            user_profile.knows_music = profile_form.cleaned_data.get("knows_music")
            user_profile.knows_drawing = profile_form.cleaned_data.get("knows_drawing")
            user_profile.knows_video_editing = profile_form.cleaned_data.get("knows_video_editing")
            user_profile.knows_animation = profile_form.cleaned_data.get("knows_animation")
            user_profile.learn_math = profile_form.cleaned_data.get("learn_math")
            user_profile.learn_singing = profile_form.cleaned_data.get("learn_singing")
            user_profile.learn_music = profile_form.cleaned_data.get("learn_music")
            user_profile.learn_drawing = profile_form.cleaned_data.get("learn_drawing")
            user_profile.learn_video_editing = profile_form.cleaned_data.get("learn_video_editing")
            user_profile.learn_animation = profile_form.cleaned_data.get("learn_animation")
            user_profile.description = profile_form.cleaned_data.get("description")
            user_profile.save()
        else:
            print("error")
        user_profile = Profile.objects.get(user=request.user)
        return redirect("learn")
        
    else:
        form = ProfileEditForm()
        return render(request, "profile_update.html", context={
            "form": form,
        })
