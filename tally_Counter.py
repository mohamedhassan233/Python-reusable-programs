class Counter():
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def click(self):
        self._value += 1

    def undo(self):
        self._value -= 1
        if self._value < 0:        #cannot click the undo button more often than the click button.
            self._value = 0

    def reset_counter(self):
        self._value = 0

tally = Counter()
tally.reset()
tally.click()
tally.click()

result = tally.getValue()

