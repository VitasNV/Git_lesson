# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)


class Tomato:
    states = {0: 'none', 1: 'flower', 2: 'green', 3: 'red'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')  # стадия созревания томата

    def is_ripe(self):
        if self._state == 3:  # проверка на зрелость
            return True
        return False


# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая.

class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]  # список объектов класса Tomato

    def grow_all(self):
        for tomato in self.tomatoes:  # Переводим каждый помидор из списка на следующий этап созревания
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():  # Проверяем все ли томаты созрели
                return False
        return True

    def give_away_all(self):
        self.tomatoes = []  # Чистим список томатов после сбора урожая


# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

class Gardener:

    def __init__(self, name, plant):  # Кто будет работать над растением
        self.name = name
        self._plant = plant  # protected

    def work(self):
        print(f'Gardener {self.name} is working')
        self._plant.grow_all()  # Садовник работает
        print(f'Gardener {self.name} finished')

    def harvest(self):
        print(f'Gardener {self.name} is harvesting')
        if self._plant.all_are_ripe():  # Если все созрели, тогда собираем урожай
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Plant is not ripe')

    @staticmethod
    def knowledge_base():  # Выводим справку по садоводству
        print('Harvesting tomatoes when they are ripe. Ripe tomato is red.')


# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

Gardener.knowledge_base()
tomato_bush = TomatoBush(2)
gardener = Gardener('Vitali', tomato_bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
