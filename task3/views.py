from django.shortcuts import render

# Create your views here.
def platform(request):
    # Создаем словарь с пунктами меню
    menu_items = {
        'menu': [
            {'title': 'Главная страница', 'url': '#'},  # Заглушка
            {'title': 'Магазин', 'url': 'games/'},     # Ссылка на магазин
            {'title': 'Корзина', 'url': 'cart/'},      # Ссылка для корзины
        ]
    }
    return render(request, 'third_task/platform.html', context=menu_items)

def games_view(request):
    # Создаем словарь с названиями игр и кнопками "Купить"
    games = {
        'games_list': [
            {'title': 'The Witcher 3: Wild Hunt', 'button': 'Купить'},
            {'title': 'Cyberpunk 2077', 'button': 'Купить'},
            {'title': 'Doom Eternal', 'button': 'Купить'},
        ]
    }
    return render(request, 'third_task/games.html', context=games)

def cart(request):
    cart = {
        'cart_list': [
            {'title': 'но вы еще ничего не купили'},
        ]
    }
    return render(request, 'third_task/cart.html', context=cart)