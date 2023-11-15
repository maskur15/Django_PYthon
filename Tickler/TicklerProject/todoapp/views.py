from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm
from django.contrib.auth import login,logout
from django.shortcuts import render, redirect,get_object_or_404
# views.py
from django.http import Http404
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login,get_user_model,authenticate
from django.utils.html import strip_tags
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from .models import Task

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
            sender_name = "TciklerApp"
            from_email = f'"{sender_name}" <sabilhasan2018@gmail.com>'

            try:
                
                send_mail(
                            mail_subject,
                            message_plain,  # Plain text version
                            from_email,
                            [email],
                            html_message=message_html,  # HTML version
                            fail_silently=False,
                        )
          
                messages.success(request,"You have scucessfully registred.Check your email and activate your account")
                return redirect('home')

            except Exception as e:
                errormsg= f"Email couldn't be sent {str(e)}"
                messages.success(request,errormsg)

                  #return render(request,'registration_success.html')  # Redirect to a success page
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

def homeView(request):
    if request.user.is_authenticated:
        task_list = Task.objects.filter(user=request.user)
        return render(request,'home.html',{'tasks':task_list})
    else:
        return render(request,'home.html')
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
        else:
            messages.success(request,"Try with correct username & password")
    return redirect('home')
    

def logoutUser(request):
    logout(request)
    return redirect('home')
    pass

def createTask(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            title = request.POST.get('task_title')
            description = request.POST.get('task_description')
            task = Task(title=title,description=description,user=request.user)
            task.save()
        #task_list = Task.objects.filter(user=request.user)
            
       # return render(request,'home.html',{'tasks':task_list})
    else:
        messages.success(request,"You must login first")
    return redirect('home')
def updateTask(request,item_id):

    if request.user.is_authenticated:
        try:
            item = get_object_or_404(Task,id=item_id)
            if request.method=='POST':
                title = request.POST.get('task_title')
                description = request.POST.get('task_description')
                item.title=title
                item.description= description
                item.save()
                messages.success(request,"Task updated successfully")
            else:
                tasks = Task.objects.filter(user=request.user).exclude(id=item_id)
                return render(request,'editForm.html',{'item':item,'tasks':tasks})
        except Http404:
            messages.success(request,"Task doesnt exist")

    return redirect('home')
def deleteTask(request,item_id):
    if request.user.is_authenticated:
        try:
            item = get_object_or_404(Task,pk=item_id)
            item.delete()
        except Http404:
            messages.success(request,"The item not found")
    else:
        messages.success(request,"You must log in first")

    return redirect('home') 
