import random

class Die:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value
    


class Player:
    def __init__(self,die,is_computer=False):
        self._die = die
        self._is_computer = is_computer

    def roll_dice(self):
        return self._die.roll()


my_die = Die()
my_player = Player(my_die)

my_player.roll_dice()
print(my_die.value)
