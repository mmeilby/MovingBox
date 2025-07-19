
import os
import sys
import time

try:
    import automationhat
except ImportError:
    import mock_automationhat as automationhat

class Controller:
    def __init__(self):
        pass

    def forward(self):
        automationhat.output.one.off()
        automationhat.output.two.off()
        # Pause.
        time.sleep(0.5)
        automationhat.output.one.on()

    def reverse(self):
        automationhat.output.one.off()
        automationhat.output.two.on()
        # Pause.
        time.sleep(0.5)
        automationhat.output.one.on()

    def left(self):
        automationhat.relay.one.off()
        automationhat.output.three.off()
        # Pause.
        time.sleep(0.5)
        automationhat.relay.one.on()

    def right(self):
        automationhat.relay.one.off()
        automationhat.output.three.on()
        # Pause.
        time.sleep(0.5)
        automationhat.relay.one.on()

    def stop(self):
        automationhat.output.one.off()
        automationhat.relay.one.off()

    def straight(self):
        automationhat.relay.one.off()

    def status(self):
        status = {}
        if automationhat.output.one.is_off():
            status["drive"] = "stopped"
        else:
            if automationhat.output.two.is_off():
                status["drive"] = "forward"
            else:
                status["drive"] = "reverse"
        if automationhat.relay.one.is_off():
            status["turn"] = "no turn"
        else:
            if automationhat.output.three.is_off():
                status["turn"] = "left"
            else:
                status["turn"] = "right"
        return status