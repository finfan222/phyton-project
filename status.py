from colorama import Fore

BAR_HAVE_HP = Fore.RED + "■" + '\033[0m'
BAR_HAVE_MP = Fore.BLUE + "■" + '\033[0m'
BAR_HAVE_CP = Fore.YELLOW + "■" + '\033[0m'
BAR_LOST = "□"
MAX_BARS = 30


class Status:
    maxHp: int = 0
    curHp: int = 0
    maxMp: int = 0
    curMp: int = 0
    maxCp: int = 0
    curCp: int = 0

    def __init__(self, curHp, maxHp, curMp, maxMp, curCp, maxCp):
        self.maxHp = maxHp
        self.curHp = curHp
        self.maxMp = maxMp
        self.curMp = curMp
        self.curCp = curCp
        self.maxCp = maxCp

    def __repr__(self):
        var = ""
        return var + "HP " + self.draw_hp_bar() + " " + str(self.curHp) + "/" + str(self.maxHp) + "\n" \
               + "MP " + self.draw_mp_bar() + " " + str(self.curMp) + "/" + str(self.maxMp) + "\n" \
               + "CP " + self.draw_cp_bar() + " " + str(self.curCp) + "/" + str(self.maxCp)

    def draw_hp_bar(self):
        percent_hp: float = self.curHp / self.maxHp
        bars_to_have: int = round(percent_hp * MAX_BARS)
        string: str = ""
        for i in range(MAX_BARS):
            if i < bars_to_have:
                string += BAR_HAVE_HP
            else:
                string += BAR_LOST
        return string

    def draw_mp_bar(self):
        percent_mp: float = self.curMp / self.maxMp
        bars_to_have: int = round(percent_mp * MAX_BARS)
        string: str = ""
        for i in range(MAX_BARS):
            if i < bars_to_have:
                string += BAR_HAVE_MP
            else:
                string += BAR_LOST
        return string

    def draw_cp_bar(self):
        percent_cp: float = self.curCp / self.maxCp
        bars_to_have: int = round(percent_cp * MAX_BARS)
        string: str = ""
        for i in range(MAX_BARS):
            if i < bars_to_have:
                string += BAR_HAVE_CP
            else:
                string += BAR_LOST
        return string
