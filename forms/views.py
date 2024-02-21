from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def forms(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        level = request.POST.get('level')
        meal = request.POST.get('meal')
        rating = request.POST.get('rating')

        # Validate that all fields are filled
        if not name or not email or not department or not level or not meal or not rating:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'forms/forms.html')

        # Validate the email domain
        if not email.endswith('@student.babcock.edu.ng'):
            messages.error(request, 'Please use your Babcock student email.')
            return render(request, 'forms/forms.html')

        # Additional email validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Please enter a valid email address.')
            return render(request, 'forms/forms.html')

        # If all validations pass, proceed to save the form
        feedback = Feedback(name=name, email=email, department=department, level=level, meal=meal, rating=rating)
        feedback.save()
        messages.success(request, 'Your response has been recorded. Thank you very much.')
        return redirect('forms')  # Make sure you have a URL pattern named 'forms' in your urls.py

    else:
        # If it's a GET request, just display the form
        return render(request, 'forms/forms.html')
