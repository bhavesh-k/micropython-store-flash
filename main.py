import json
from machine import Pin
from time import sleep

# load the config file from flash
with open('config.json') as f:
    config = json.load(f)

# LED and button
led = Pin(2, Pin.OUT)
btn = Pin(0)

# load LED state from config file
if config['is_led_on']:
    led.value(1)
else:
    led.value(0)

# saves config to flash
def save_config():
    with open('config.json', 'w') as f:
        json.dump(config, f)
    
# use button to toggle LED
while True:
    if btn.value() == 0:
        led.value(not led.value())
        config['is_led_on'] = led.value()
        save_config()
        
    sleep(0.5)
        