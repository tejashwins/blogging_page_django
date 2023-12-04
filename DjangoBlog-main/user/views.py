from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
def register(request):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        form.save()
        messages.success(request, f'Account Created for the uesr {username} successfully!')
        return redirect('login')

    else:
        form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm(request.POST, instance=request.user)
    f_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    if u_form.is_valid() and f_form.is_valid():
        u_form.save()
        f_form.save()
        messages.success(request, f'Profile updated successfully!')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
    return render(request, 'user/profile.html', context)
