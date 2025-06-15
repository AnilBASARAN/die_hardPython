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
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_dice(self):
        return self._die.roll()
    
class Game_round:
    def __init__(self):
    
        
        print("*********This is the new Round*********")
        input("*****Press Any Key to Roll the Dice*****")





class DiceGame:
    def __init__(self,player,computer):
         self._player = player
         self._computer = computer
         self._round = round

    def play(self):
        print("*****************************")
        print("***Welcome to My Dice Game***")
        print("*****************************")
        while True:
            self.play_round()

    def play_round(self):
        print("------New Round------")
        input("----Press Any Key----")

        player_value = self._player.roll_dice()
        computer_value = self._computer.roll_dice()