# freelance_dvmn
Сервис поиска задач на фриланс
Бот, в котором заказчики могут заказывать небольшие фичи для своих проектов, а фрилансеры могут оперативно выполнять заказы за награду, 
буквально в тот же день, как заказ был опубликован.

## Установка
Скачайте код:
```sh
git clone https://github.com/PaSeRouS/freelance_dvmn.git
```

Перейдите в каталог проекта:
```sh
cd freelance_dvmn
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.10

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`.
Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии.

## Установка виртуального окружения и настройка зависимостей
В каталоге `freelance_dvmn/` создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```
## Переменные окружения
В каталоге `freelance_dvmn/` создайте файл `.env` для хранения переменных окружения
#### SECRET_KEY
Определите переменную окружения `SECRET_KEY`:
```sh
SECRET_KEY=<Ваш секретный ключ>
```
#### TG_TOKEN
* Через поиск телеграм найдите бот @BotFather. 
* Отправьте `/start` для получения списока всех его команд.
* Выберите команду /newbot - бот попросит придумать имя вашему новому боту. 
* Сохраните полученный токен в переменной `TG_TOKEN` в файле `.env`:

```
TG_TOKEN=<Токен для вашего бота>
```

#### PAYMENT_PROVIDER_TOKEN
* В боте `@BotFather` неберите команду `/mybots`
* Выберите только что созданного бота
* Нажмите кнопку `Payments`
* Выберите платежную сиситему
* Выберите тестовый режим оплаты
* Вас перенаправит на бот платежной системы. 
Зарегистрируйте бот в платежной системе, после чего в чате с `@BotFather` появится ваш платежный токен
* Сохраните токен в переменной `PAYMENT_PROVIDER_TOKEN` в файле `.env`

## База данных
Создайте файл базы данных `db.sqite3` и отмигрируйте её следующей командой:

```sh
python manage.py migrate
```

Создайте суперпользователя:
```
python manage.py createsuperuser
```

Запустите бот командой:

```sh
python manage.py start_bot
```

Для доступа в админку запустите сервер комнадой:
```
python manage.py runserver
```
Админка будет доступна в браузере по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/).

# Над проектом работали
[Павел Серов](https://github.com/PaSeRouS)

[Эльнар Менгельбаев](https://github.com/elnarmen)

[https://github.com/leenythebear](https://github.com/leenythebear)
