# Библиотеки нужные для подсветки:
# Fore - цвет самого текста
# Back - цвет заднего фона ЗА текстом (типо можно сделать красный текст на жёлтом фоне и т.д.)
from colorama import Fore, Back


def colored(textColor, backgroundColor, text):
    return textColor + backgroundColor + str(text) + '\033[0m'


def colored0(textColor, value):
    return textColor + str(value) + '\033[0m'


# '\033[0m' = это такой цвет в ANSI кодировке, тебе пока это знать не обязательно, просто понимай это как некий "код" к цветам внутри машины

class Weapon:
    name = None
    attack = None
    durability = None
    speed = None
    price = None
    type = None

    def set_attack(self, attack):
        self.attack = attack
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_durability(self, durability):
        self.durability = durability
        return self

    def set_speed(self, speed):
        self.speed = speed
        return self

    def set_price(self, price):
        self.price = price
        return self

    def set_type(self, _type):
        self.type = _type
        return self

    def info(self):
        print(
            colored(Fore.YELLOW, Back.BLACK, "Характеристики:"),
            colored0(Fore.YELLOW, "\n\tНаименование: "), colored0(Fore.CYAN, self.name),
            colored0(Fore.YELLOW, "\n\tУрон: "), colored0(Fore.GREEN, self.attack),
            colored0(Fore.YELLOW, "\n\tЦена: "), colored0(Fore.GREEN, self.price),
            colored0(Fore.YELLOW, "\n\tПрочность: "), colored0(Fore.GREEN, self.durability),
            colored0(Fore.YELLOW, "\n\tСкорость атаки: "), colored0(Fore.GREEN, self.speed),
            colored0(Fore.YELLOW, "\n\tТип оружия: "), colored0(Fore.GREEN, self.type)
        )

    def decrease_durability(self, value: int):
        self.durability -= value
        if self.durability <= 0:
            print("Оружие сломалось!")
            return True
        else:
            print("Прочность оружия уменьшена на " + value)
            return False
