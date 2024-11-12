from django.shortcuts import render

# Create your views here.

def platform(request):
    title = 'Бытовая техника'
    text = 'Главная страница'

    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/platform.html', context)

def shop(request):
    title = 'Бытовая техника'
    text = 'Товары'
    text1 = 'Ноутбук Huawei MateBook D 16'
    text2 = 'Телевизор Hisense 50E7NQ'
    text3 = 'Миксер VITEK VT-1494'
    text4 = 'Купить 💳'
    text5 = '🔙 Вернуться обратно'
    text6 = 'Добавить в корзину ✅'

    context = {
        'title': title,
        'text': text,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'text4': text4,
        'text5': text5,
        'text6': text6
    }
    return render(request, 'third_task/shop.html', context)

def cart(request):
    title = 'Бытовая техника'
    text = 'Корзина'
    text1 = 'Ноутбук Huawei MateBook D 16'
    text2 = 'Телевизор Hisense 50E7NQ'
    text3 = 'Миксер VITEK VT-1494'
    text4 = 'Купить 💳'
    text5 = '🔙 Вернуться обратно'
    text6 = 'Удалить 🗑'
    text7 = 'Сделать заказ!'

    context = {
        'title': title,
        'text': text,
        'text1': text1,
        'text2': text2,
        'text3': text3,
        'text4': text4,
        'text5': text5,
        'text6': text6,
        'text7': text7
    }
    return render(request, 'third_task/cart.html', context)