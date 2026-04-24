from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Project, Skill,  Contact

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html', {
        'projects': projects,
        'skills': skills,
    })

def projects(request):
    category = request.GET.get('category', 'all')
    if category == 'all':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category=category)
    return render(request, 'projects.html', {
        'projects': projects,
        'active_category': category,
    })

def about(request):
    skills = Skill.objects.all()
    return render(request, 'about.html', {'skills': skills})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(name=name, email=email, message=message)

        # Send email
        send_mail(
            subject=f'Portfolio Contact from {name}',
            message=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
        messages.success(request, 'Message sent successfully!')

    return render(request, 'contact.html')
import os
from django.http import FileResponse, Http404

def resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'resume.pdf')

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)

    raise Http404("Resume not found")