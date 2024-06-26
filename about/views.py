from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Contact
from .forms import ContactForm

def about_page(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {
            'about': about
        },
    )

def contact_page(request):
    """
    View to the contact form
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request=request)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                "Thanks for your inquiry! We will get back to you shortly."
            )
            return redirect('home')
    else:
        contact_form = ContactForm(request=request)
    
    return render(
        request, 
        "about/contact.html", 
        {
            'contact_form': contact_form
        },
    )