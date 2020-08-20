try:
    import vk_api
except:
    print('Установите необходимые модули через команду \'$ pip3 install -r requirements.txt\' перед запуском скрипта.'); exit()

import os

def clear_screen():
    os.system('cls') if os.name == 'nt' else os.system('clear')

clear_screen()

while True:
    login = input('VK login: ')
    password = input('VK password: ')

    try:
        vk_session = vk_api.VkApi(login, password, app_id='2685278', auth_handler = lambda: [input('VK 2FA code: '), False])
        vk_session.auth()
    except vk_api.exceptions.LoginRequired:
        print('Логин не может быть пустым!')
    except vk_api.exceptions.PasswordRequired:
        print('Пароль не может быть пустым!')
    except vk_api.exceptions.BadPassword:
        print('Неверный пароль!')
    else:
        print('Вы в VK!'); break

vk = vk_session.get_api()

vk.wall.post(message='Hello world! :D')
