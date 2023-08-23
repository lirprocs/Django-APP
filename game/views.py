from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def blockrain_game(request):
    return render(request, 'game/game.html')
