class Die:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,new_color):
        self._value = new_color

    @value.deleter
    def value(self):
        del self._value