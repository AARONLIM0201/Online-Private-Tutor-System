from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from account.models import Account
from django.contrib.auth.decorators import login_required

def home(request):

    """Renders the home page."""
    assert isinstance(request, HttpRequest)


# if request.user.is_authenticated:
#     return(redirect('/menu'))
# else:
    return render(
    request,
    'app/homepage.html',
    {
        'title':'Home Page',
        'year': datetime.now().year,
    }
)




def about(request):
    context = {
        'title': 'About TutorConnect',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context
    )

def bookings(request):
    context = {
        'title': 'Booking',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/bookings.html',
        context
    )

def sessions(request):
    context = {
        'title': 'Sessions',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/sessions.html',
        context
    )

def payment(request):
    context = {
        'title': 'Payments',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payment.html',
        context
    )

def progressreport(request):
    context = {
        'title': 'Progress Report',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/progressreport.html',
        context
    )

def chat(request):
    context = {
        'title': 'Chat',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/chat.html',
        context
    )

def classes(request):
    context = {
        'title': 'Classes',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/classes.html',
        context
    )

def assignments(request):
    context = {
        'title': 'Assignments',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/assignments.html',
        context
    )

def resources(request):
    context = {
        'title': 'Resources',
        'message': 'This application processes ...',
        'year': datetime.now().year,
    }
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/resources.html',
        context
    )

# @login_required # This is a decorator that ensures that the user is logged in before they can access the menu page
# def menu(request):
#     role = request.user.account.role
#     if role == 'Tutor':
#         context = {
#             'title': 'Menu',
#             'message': 'Welcome to the menu page',
#             'year': datetime.now().year,
#         }
#         return render(request,'app/home.html',context)
    
#     elif role == 'Student':
#         context = {
#         'title': 'Menu',
#         'message': 'Welcome to the menu page',
#         'year': datetime.now().year,
#     }
#         return render(request,'app/about.html',context)
    
#     else:
#         context = {
#         'title': 'Menu',
#         'message': 'Welcome to the menu page',
#         'year': datetime.now().year,
#     }
#         return render(request,'app/register.html',context)
    