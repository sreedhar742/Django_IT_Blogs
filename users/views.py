from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.conf import settings
from .tasks import sending_email

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}')
            subject = 'Welcome to blogs!'
            message = f'Hi {username}, thank you for registering on Blogs account.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]

            # Send email asynchronously
            sending_email.delay(message, subject, email_from, recipient_list)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')

            username = request.user.username
            email = request.user.email
            subject = "Your Profile is updated"
            message = f'Mr. {username}, your profile has been updated with the changes you made.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]

            # Send email asynchronously
            sending_email.delay(message, subject, email_from, recipient_list)
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)



# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from django.core.mail import send_mail
# from django.conf import settings
# # Create your views here.
# from .tasks import sending_email
# def register(request):
#     if request.method=='POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             email=form.cleaned_data.get('email')
#             messages.success(request, f'Account created for {username}')
#             subject = 'Welcome to blogs!'
#             message = f'Hi {username}, thank you for registering on Blogs account.'
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [email,]
            
#             # try:
#             #     send_mail(subject, message, email_from, recipient_list)
#             # except Exception as e:
#             #     print(f"Error sending email: {e}")
#             sending_email(message,subject,email_from,recipient_list)
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form':form})

# from django.contrib.auth.models import User

# @login_required
# def profile(request):
#     if request.method=='POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             print(request.user)
#             user=User.objects.get(username=request.user)
#             username=user.username
#             email=user.email
#             subject="Your Profil is updated"
#             message=f'Mr.{username} your profile is updated changes done by you' 
#             email_from=settings.EMAIL_HOST_USER
#             recipient_list=[email]
#             try:
#                 send_mail(subject,message,email_from,recipient_list)
#             except Exception as e:
#                 print(f"Error sending email: {e}") 
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     context = {
#         'u_form':u_form,
#         'p_form':p_form
#     }
#     return render(request, 'users/profile.html', context)



# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             # Save user information
#             u_form.save()
            
#             # Handle the image data
#             if p_form.cleaned_data['image_data']:
#                 # Read the uploaded image as bytes and save it
#                 image_file = p_form.cleaned_data['image_data']
#                 request.user.profile.image_data = image_file.read()  # Store as binary
#             else:
#                 # If no new image is provided, keep the existing one
#                 request.user.profile.image_data = request.user.profile.image_data
            
#             request.user.profile.save()  # Save the profile
            
#             messages.success(request, f'Your account has been updated!')
            
#             # Send email notification about the profile update
#             username = request.user.username
#             email = request.user.email
#             subject = "Your Profile is updated"
#             message = f'Mr. {username}, your profile is updated with changes made by you.'
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = [email]
#             try:
#                 send_mail(subject, message, email_from, recipient_list)
#             except Exception as e:
#                 print(f"Error sending email: {e}")
                
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'users/profile.html', context)