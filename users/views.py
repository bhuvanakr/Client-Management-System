from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# def password_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('password_change')
#         else:
#             messages.error(request, 'Please correct the error below Mee.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'registration/password_change.html', {
#         'form': form
#     })

# Create your views here.
