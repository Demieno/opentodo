
# OpenTODO - простая cистема управления задачами

---

**Данный форк проекта адаптирован для работы с Django версии 2.1 и новее.**

---

## Установка и запуск

Для установки данного проекта используется менеждер пакетов Pipenv (https://docs.pipenv.org).

База данных по умолчанию - SQLite 3.

1. Cкопируйте код репозитория.
2. Выполните в директории проекта `pipenv install`.
3. Переключитесь в субконсоль `pipenv shell`.
4. Выполните миграции БД `python manage.py migrate`.
5. Создайте суперпользователя `python manage.py createsuperuser`.
6. Запустите встроенный веб-сервер для разработки `python manage.py runserver`
7. Перейдите в браузере по адресу http://127.0.0.1:8000/

## Новое в версии 2.0.0-dev (5 января 2019)

+ Выполнен перенос кодовой базы для запуска на новейшей версии Django 2.1.
+ Использование Pipenv для управления зависимостями.
+ Использование внешнего пакета `django-annoying`.
+ Миграции БД.

## Новое в версии 0.91 (31 марта 2009)

+ Теперь для перехода к задаче из списка достаточно кликнуть по ряду таблицы (не обязательно по названию задачи).
+ Ссылки для автоматической вставки html-тегов в textarea (описание задач и проектов, комментарии).

Также переработан парсинг html, исправлены ошибки. Библиотека BeautifulSoap больше не используется.

Исправлен баг - при ответе на комментарий его автору не приходило уведомление по почте.

Теперь в настройках MEDIA_URL не имеет значения, есть слэш в конце или нет, все корректно работает в любом случае.


## Новое в версии 0.9 (22 марта 2009)

+ Разграничение доступа пользователей к проектам
+ Фильтр - по автору, исполнителю, статусу, названию задачи
+ Ответ на комментарии - при ответе автор комментария получает уведомление по e-mail
+ Разметка текста - в описании проектов, задач и тексте комментариев разрешены некоторые html-теги


## Ссылки на оригинальную версию (Django 1.5)

* Описание, инструкция по установке, релизы: http://code.google.com/p/opentodo/
* Исходный код для на GitHub: http://github.com/mgrigoriev/opentodo/


## Лицензия 

GNU General Public License v3

## Авторы

(c) 2008-2012, Михаил Григорьев (<mgrigoriev@gmail.com>)
(c) 2019, Евгений Дементьев (<devg@ya.ru>)
