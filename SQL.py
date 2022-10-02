#  Создайте новую Базу данных. Поля: id, 2 целочисленных поля. Целочисленные поля заполняются рандомно от 0 до 9.
#  Посчитайте среднее арифметическое всех элементов без учёта id.
#  Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД
#
import sqlite3
import random  # для заполнения данных рандомно

conn = sqlite3.connect('dz.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')

for i in range(5):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''', (a, b))  # для заполнения данных
# conn.commit()  # для запоминания данных в базе
cursor.execute('''SELECT col_1, col_2 FROM tab_1''')  # вызываем данные без id для подсчета среднего значения
k = cursor.fetchall()  # вызываем атрибут
print(k, len(k))

aver = []
for i in k:
    aver.append((sum(i) / len(i)))  # добавляем средние значения по каждому кортежу в список
    if (sum(aver) / len(aver)) > len(k):  # среднее арифметическое всех элементов в базе данных
        cursor.execute('''DELETE FROM tab_1 WHERE id=4''')  # удаляем четвертую запись по условию задачи
        cursor.execute('''SELECT * FROM tab_1''')  # вызываем данные с id, для выполнения условия удаления
        k = cursor.fetchall()  # вызываем атрибут

print(aver)  # список средних значений кортежей
print('average values', sum(aver) / len(aver))  # среднее значение, для понимания выполнения задачи
print(k, len(k))  # если сработает условие, длинна будет меньше на одну запись id 4
