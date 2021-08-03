class Counter:
    def __init__(self, init_value=0):
        self._value = init_value

    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1

    @property
    def value(self):
        return self._value
