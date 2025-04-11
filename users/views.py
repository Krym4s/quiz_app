from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileEditForm
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

User = get_user_model()

def logout_view(request):
    logout(request)
    messages.success(request, "Вы успешно вышли из системы")
    return redirect('home')

@login_required
def profile(request):
    """Страница профиля пользователя"""
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    """Редактирование профиля"""
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлён!')
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    
    return render(request, 'users/edit_profile.html', {'form': form})
