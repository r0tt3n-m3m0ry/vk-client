try:
    import vk_api
except:
    print('Установите необходимые модули через команду \'$ pip3 install -r requirements.txt\' перед запуском скрипта.'); exit()

import time
import os

def clear_screen():
    os.system('cls') if os.name == 'nt' else os.system('clear')

clear_screen()

try:
    while True:
        try:
            vk_session = vk_api.VkApi(login=input('VK login: '), password=input('VK password: '), app_id='2685278', auth_handler = lambda: [input('VK 2FA code: '), False])
            vk_session.auth()
        except vk_api.exceptions.LoginRequired:
            print('Логин не может быть пустым!')
        except vk_api.exceptions.PasswordRequired:
            print('Пароль не может быть пустым!')
        except vk_api.exceptions.BadPassword:
            print('Неверный пароль!')
        except vk_api.exceptions.Captcha as captcha:
            captcha_key = input(f'Enter captcha code ({captcha.get_url()}): ')
            captcha.try_again(captcha_key)
        else:
            print('Вы в VK!'); os.remove('vk_config.v2.json'); time.sleep(1.25); break

    vk = vk_session.get_api()
    
    clear_screen()

    account_info = vk.account.getProfileInfo()
    
    print(f"Добро пожаловать, {account_info['first_name']} {account_info['last_name']}! :D\nВаш статус - {vk.status.get()['text']}")

    if input('Хотите его изменить? (Д/Н) > ').lower() == 'д':
        try:
            vk.status.set(text=input('Введите текст для нового статуса: '))
        except:
            print('Статус не был изменен!')
        else:
            print('Статус установлен!')
    else:
        print('Ну и славно :3 Этот статус тоже неплох, ня <3')

    print('\nДо скорого! :D')

except KeyboardInterrupt:
    print('\n\nДосвиданья >:D'); exit()
