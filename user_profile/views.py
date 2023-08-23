from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile


@login_required
def profile(request):
    return render(request, 'user_profile/profile.html')


def redprofile(request):
    user = request.user

    try:
        profile = user.profile
    except Profile.DoesNotExist:
        # Создаем новый профиль для пользователя, если его нет
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'user_profile/redprofile.html', context)


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile

        # Удаление пользователя
        user.delete()

        # Удаление профиля
        profile.delete()

        return redirect('home')

    return render(request, 'user_profile/delete_account.html')