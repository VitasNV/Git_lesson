# 1. Сформулируйте SQL запрос для создания таблицы movies.
# Поля: movie_id, name TEXT, release_year INTEGER, genre TEXT, country TEXT.
# 2. Создать функции:
#   1. Добавить фильм (заполнение делать с клавиатуры).
#   2. Получения данных обо всех фильмах.
#   3. Получения данных об одном фильме по id.
#   4. Получения данных об фильмах по стране изготовления.
#   0. Выход
# 3. Функции вызывать в цикле, чтоб у пользователя был выбор.
#
# 1 ('Вышка', 2022, 'триллер', 'Великобритания'))
# 2 ('Иди и смотри', 1985, 'драма', 'Беларусь'),
# 3 ('Молодой человек', 2022, 'комедия', 'Россия'),
# 4 ('Аватар', 2009, 'фантастика', 'США'),
# 5 ('Джентльмены', 2019, 'криминал', 'Великобритания'),
# 6 ('Приглашение', 2022, 'ужасы', 'США'),
# 7 ('Слепой', 2012, 'боевик', 'Франция'),
# 8 ('Ван Хельсинг', 2004, 'фэнтези', 'США'))

import sqlite3 as sq

conn = sq.connect('movies.db')  # создаем базу данных для фильмов расширение .db
cursor = conn.cursor()  # позволяет нам взаимодействовать с базой данных и добавлять записи

cursor.execute('''CREATE TABLE IF NOT EXISTS movies(movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT, release_year INTEGER, genre TEXT, country TEXT)''')  # заполняем шапку таблицы


def add_movies():  # Функция добавления фильмов (заполнение делаем с клавиатуры)
    a = input('name: ')
    b = int(input('release: '))
    c = input('genre: ')
    d = input('country: ')
    cursor.execute('''INSERT INTO movies(name, release_year, genre, country) VALUES (?, ?, ?, ?)''', (a, b, c, d))
    return cursor.fetchall()  # вызываем обязательный атрибут


def all_movies():  # Получения данных обо всех фильмах.
    k_all = cursor.execute('''SELECT * FROM movies''')  # присвоим переменную k для возможности итерации
    print('Список movies:')
    for i in k_all:
        print(', '.join([str(i_2) for i_2 in i]))  # для удобства просмотра делаем один фильм в одну строку


def choice_movies():  # Для выбора фильма по id.
    i = int(input('movies_id: '))
    k_choice = cursor.execute('''SELECT * FROM movies WHERE movie_id=?''', (i,))
    for i in k_choice:
        print(', '.join([str(i_2) for i_2 in i]))  # для удобства просмотра делаем фильм читабельно в одну строку


def country_movies():  # Для выбора фильмов по стране происхождения.
    cursor.execute('''SELECT country VALUE FROM movies''')  # вынимаем из столбца страны, которые представлены
    countries = cursor.fetchall()
    country = set()  # Пустой список стран для сортировки, чтобы не было повторов берем список из множества
    for i in countries:
        country.add(', '.join([str(i_2) for i_2 in i]))  # для удобства просмотра делаем читабельно в одну строку
    print('В списке фильмы, производства: ', country)  # показываем какие страны
    d = input('country: ')
    k_country = cursor.execute('''SELECT * FROM movies WHERE country=?''', (d,))
    for i in k_country:
        print(', '.join([str(i_2) for i_2 in i]))  # для удобства просмотра делаем один фильм в одну строку


def exit_movies():  # Функция выхода
    print('Спасибо за просмотр!')


while True:
    print('''Сделайте свой выбор:
            1. Добавить фильм (заполнение делать с клавиатуры).
            2. Получения данных обо всех фильмах.
            3. Получения данных об одном фильме по id.
            4. Получения данных об фильмах по стране изготовления.
            0. Выход''')
    x = int(input('Введите свой выбор: '))
    if x == 1:
        print(add_movies())

    elif x == 2:
        all_movies()

    elif x == 3:
        choice_movies()

    elif x == 4:
        country_movies()

    elif x == 0:
        exit_movies()
        break

conn.commit()
