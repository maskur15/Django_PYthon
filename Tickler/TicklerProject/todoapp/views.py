from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
# views.py
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login,get_user_model
from django.utils.html import strip_tags
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages

User = get_user_model()

def registration_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            gender = form.cleaned_data['gender']
            country = form.cleaned_data['country']
            # Add other fields as needed

            # Create a user with is_active=False
            user = User.objects.create_user(
                username= username,
                email=email,
                password=password,
                gender=gender,
                country=country,
                is_active=False  # Set the user as inactive until email verification
            )
            # Generate a verification token

            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
             # Construct the domain dynamically based on the current request
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Construct the domain dynamically based on the current request
            domain = request.build_absolute_uri(reverse('activate', args=[uid, token]))

            message_html = render_to_string(
                'registration/activation_email.html',
                {
                    'user': user,
                    'domain':domain,
                    'uid': uid,
                    'token': token,
                },
            )
            message_plain = strip_tags(message_html)

            # Send the email with both HTML and plain text versions
            send_mail(
                mail_subject,
                message_plain,  # Plain text version
                'sabilhasan2018@gmail.com',
                [email],
                html_message=message_html,  # HTML version
                fail_silently=False,
            )

            return render(request,'registration_success.html')  # Redirect to a success page
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})






def activate_account(request, uidb64, token):
    User = get_user_model()

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)  # Log the user in

        messages.success(request, 'Your account has been activated. You are now logged in.')
        return redirect('home')  # Redirect to the home page or any desired destination upon activation

    # Activation failed
    messages.error(request, 'Invalid activation link.')
    return redirect('login')  # Redirect to the login page or an error page

def loginUser(request):
    return render(request,'home.html')

def logoutUser(request):
    logout(request)
    return redirect('home')
    pass
def createTask(request):
    if request.method=='POST':
        pass 
