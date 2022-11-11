import os
import time

from weapons import *
from creature import *
from num import *
from status import Status

######################################## Тупое создание предмето используя ООП принципы (классы)
print("===Загрузка всего арсенала===")
spear = Weapon() \
    .set_type("Копьё") \
    .set_price(15) \
    .set_name("Копьё пламенной смерти") \
    .set_speed(1.5) \
    .set_attack(10) \
    .set_durability(100)
sword = Weapon() \
    .set_type("Меч") \
    .set_price(35) \
    .set_name("Клинок рассекающий демонов") \
    .set_speed(0.66) \
    .set_attack(7) \
    .set_durability(88)
axe = Weapon() \
    .set_type("Топор") \
    .set_price(25) \
    .set_name("Топор Огра") \
    .set_speed(2.2) \
    .set_attack(40) \
    .set_durability(200)

############################################################### Создаём контейнер (хранилище) предметов глобально и кладём то, что создали выше
storage: Weapon = {
    "1": spear,
    "2": sword,
    "3": axe
}

############################################################### Создаём глобальные бабки и выбор (типы я указал явно)
gold: int = 0
choice: str = ""


class Test:
    var = None

    def __init__(self, var=100):
        self.var = var

strg = {
    1: Test(),
    2: Test()
}
t: Test = Test()
print(strg[1].var)

# Ответ игрока на input (ввод данных с клавы)
def answer():
    global gold
    global choice
    print("Ваш выбор: ", end="")
    choice = input()
    if choice.startswith("/"):
        print(colored0(Fore.GREEN, "Найдена админ команда!"))
        match choice:
            case "/greedisgood":
                gold = 999
                print(colored0(Fore.GREEN, "Текущее кол-во золота: " + str(gold)))


# Вопрос который задаёт торгаш
def question():
    print("Что ты хочешь купить? В моём ассортименте куча барохла!")


# Бизнесс логика покупки предмета
def buy(wpn: Weapon, cost: int):
    global gold
    if gold >= cost:
        gold -= cost
        print("Вы приобрели " + colored0(Fore.YELLOW, wpn.name) + "!")
    else:
        print(colored0(Fore.RED, "У вас недостаточно золота!"))


# Вечный цикл
while True:
    status: Status = Status(620, 4327, 12, 33, 1200, 3757)
    print(status)

    ############################# Продавец запрашивает товар
    print("Добрый день дорогой путник. Что ты желаеш приобрести? (Ваше золото: " + colored0(Fore.GREEN, gold) + ")")
    for key in storage:  # цикл по всем прдметам в нашем хранилище
        weapon: Weapon = storage[key]  # переменная с каждым предметом в хранилище
        name: str = colored0(Fore.YELLOW, weapon.name)  # переменная с явным типом = имя премета
        price: int = colored0(Fore.CYAN, weapon.price)  # переменная с ценой предмета
        print("[" + key + "] " + name + " ~" + price + " золотых.")  # принтуем каждый предмет в формате:
        # [порядковый номер предметап в хранилище]
        # имя предмета
        # цена прдемета
        # " золотых."

    ############################# Игрок выбирает
    answer()  # функция реализующая выбор игрока

    ############################# Обработка нашего выбора
    try:
        # создаём переменную предмета который будем покупать (который выбрали)
        item: Weapon = storage[choice]
        # вызываем логику покупки предмета
        buy(item, item.price)
    except:
        # т.к. у нас нет более 3-ёх предметов, самые умные крупки могут выбрать > 3 или <= 0 для таких готовим перехват исключения
        # исключение появляется т.к. в случае ввода 4 я выйду за границы хранилища
        # нижний print это как бы "обработка" моего исключения
        print(colored0(Fore.RED, "Этого товара у меня нет! Проваливай и не трать моё время!"))

    player: Player = Player()
    player2: Player = Player()

    try:
        player.target.name
    except:
        print("Цель не найдена или = null.")

    player.set(player2)
    print("Цель = " + player.target.name)

    # идём спать на 3 секунды
    # time.sleep(3)
