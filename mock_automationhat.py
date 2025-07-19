# mock_automationhat.py

import random

class AnalogLogic:
    def __init__(self, name):
        self.name = name

    def read(self):
        # Returner en fiktiv analogværdi mellem 0 og 24
        return round(random.uniform(0, 24), 2)

class Analog:
    def __init__(self):
        self.one = AnalogLogic("one")
        self.two = AnalogLogic("two")
        self.three = AnalogLogic("three")
        self._channels = [self.one, self.two, self.three]

    def __call__(self):
        return self._channels

    def __getitem__(self, index):
        return self._channels[index]

class InputLogic:
    def __init__(self, name):
        self.name = name
        self.value = 0

    def read(self):
        # Returner en fiktiv analogværdi mellem 0 og 1
        self.value = round(random.uniform(0, 24), 2)
        return 1 if self.value > 3 else 0

    def is_on(self):
        return self.value > 3

    def is_off(self):
        return self.value < 1


class Input:
    def __init__(self):
        self.one = InputLogic("one")
        self.two = InputLogic("two")
        self.three = InputLogic("three")
        self._channels = [self.one, self.two, self.three]

    def __call__(self):
        return self._channels

    def __getitem__(self, index):
        return self._channels[index]

class OutputLogic:
    def __init__(self, name):
        self.name = name
        self.value: bool = False

    def write(self, value):
        if value > 0:
            self.value = True
        else:
            self.value = False

    def toggle(self):
        if self.is_on():
            self.off()
        else:
            self.on()

    def on(self):
        self.value = True

    def off(self):
        self.value = False

    def is_on(self) -> bool:
        return self.value

    def is_off(self) -> bool:
        return not self.value

class Output:
    def __init__(self):
        self.one = OutputLogic("one")
        self.two = OutputLogic("two")
        self.three = OutputLogic("three")
        self._channels = [self.one, self.two, self.three]

    def __call__(self):
        return self._channels

    def __getitem__(self, index):
        return self._channels[index]

class RelayLogic:
    def __init__(self, name):
        self.name = name
        self.value: bool = False

    def write(self, value: bool):
        self.value = value

    def toggle(self):
        if self.is_on():
            self.off()
        else:
            self.on()

    def on(self):
        self.write(True)

    def off(self):
        self.write(False)

    def is_on(self) -> bool:
        return self.value

    def is_off(self) -> bool:
        return not self.value

class Relay:
    def __init__(self):
        self.one = RelayLogic("one")
        self._channels = [self.one]

    def __call__(self):
        return self._channels

    def __getitem__(self, index):
        return self._channels[index]


analog = Analog()
input = Input()
output = Output()
relay = Relay()

def is_automation_hat() -> bool:
    return False
