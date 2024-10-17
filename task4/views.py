from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')


def games_view(request):
    games = ['The Witcher 3: Wild Hunt', 'Cyberpunk 2077', 'Doom Eternal']
    return render(request, 'fourth_task/games.html', {'games': games})

def cart_view(request):
    return render(request, 'fourth_task/cart.html')