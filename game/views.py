from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def tic_tac_toe_view(request):
    return render(request, 'game/game.html')
