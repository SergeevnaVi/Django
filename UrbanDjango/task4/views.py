from django.shortcuts import render

# Create your views here.

def platform(request):
    title = 'Бытовая техника'
    text = 'Главная страница'

    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/platform.html', context)

def shop(request):
    title = 'Бытовая техника'
    text = 'Товары'
    products = ['Ноутбук Huawei MateBook D 16', 'Телевизор Hisense 50E7NQ', 'Миксер VITEK VT-1494']
    text4 = 'Купить 💳'
    text5 = '🔙 Вернуться обратно'
    text6 = 'Добавить в корзину ✅'

    context = {
        'title': title,
        'text': text,
        'products': products,
        'text4': text4,
        'text5': text5,
        'text6': text6
    }
    return render(request, 'fourth_task/shop.html', context)

def cart(request):
    title = 'Бытовая техника'
    text = 'Корзина'
    products = ['Телевизор Hisense 50E7NQ', 'Миксер VITEK VT-1494']
    text4 = 'Купить 💳'
    text5 = '🔙 Вернуться обратно'
    text6 = 'Удалить 🗑'
    text7 = 'Сделать заказ!'

    context = {
        'title': title,
        'text': text,
        'products': products,
        'text4': text4,
        'text5': text5,
        'text6': text6,
        'text7': text7
    }
    return render(request, 'fourth_task/cart.html', context)
