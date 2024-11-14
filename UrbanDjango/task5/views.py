from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
def sign_up_by_django(request):
    users = ['Alice124', 'golf_club', 'Peter_45', 'juliet_star']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = int(request.POST.get('age', 0))

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return HttpResponse(f'Приветствуем, {username}!')
        else:
            info['error'] = 'Некорректные данные'

        context = {
            'form': form,
            'info': info
        }
        return render(request, 'fifth_task/registration_page.html', context)

    else:
        form = UserRegister()
        context = {
            'form': form,
            'info': info
        }
        return render(request, 'fifth_task/registration_page.html', context)



def sign_up_by_html(request):
    users = ['Alice124', 'golf_club', 'Peter_45', 'juliet_star']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error']  = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f'Приветствуем, {username}!')

    context = {
        'info': info
    }
    return render(request, 'fifth_task/registration_page.html', context)
