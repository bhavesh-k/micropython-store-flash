import json
from machine import Pin
from time import sleep

# load the config file from flash
with open("config.json") as f:
    config = json.load(f)

# init LED and button
led = Pin(2, Pin.OUT)
btn = Pin(0)


def save_config():
    """function to save the config dict to the JSON file"""
    with open("config.json", "w") as f:
        json.dump(config, f)


# load LED state from config file
led.value(config["is_led_on"])

# use button to toggle LED
while True:
    if btn.value() == 0:
        led.value(not led.value())
        config["is_led_on"] = led.value()
        save_config()

    sleep(0.5)
