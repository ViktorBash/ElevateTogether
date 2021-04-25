from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Connection
from django.contrib.auth.models import User
from mysite.core.models import Profile

# Create your views here.
@login_required
def chatroom_student_side(request, chat_uuid):
    the_connection = Connection.objects.get(link=chat_uuid)
    mentor = the_connection.mentor
    link = the_connection.link
    return render(request, "chatroom_for_student.html", context={
        "mentor": mentor,
        "link": link,
    })


@login_required
def create_chat_by_student(request, user_uuid):
    mentor_profile = Profile.objects.get(link=user_uuid)
    mentor = mentor_profile.user
    new_connection = Connection.objects.create(mentor=mentor, student=request.user)
    return redirect("chatroom_student_side", chat_uuid=new_connection.link)
    
@login_required
def chatroom_mentor_side(request, chat_uuid):
    the_connection = Connection.objects.get(link=chat_uuid)
    student = the_connection.student
    link = the_connection.link
    return render(request, "chatroom_for_mentor.html", context={
        "student": student,
        "link": link,
    })

@login_required
def create_chat_by_mentor(request, user_uuid):
    student_profile = Profile.objects.get(link=user_uuid)
    student = student_profile.user
    new_connection = Connection.objects.create(mentor=request.user, student=request.user)
    return redirect("chatroom_mentor_side", chat_uuid=new_connection.link)

