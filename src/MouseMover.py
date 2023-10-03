import pyautogui
import time
import logging
import subprocess

class MouseMover:
    def __init__(self, callback=None):
        self.should_run = True
        self.callback = callback
        self.logger = logging.getLogger('MouseMover')
        self.caffeinate_process = None

    def start_moving(self):
        try:
            self.caffeinate_process = subprocess.Popen(['caffeinate', '-d'])
            interval = 5  # 5 seconds
            while self.should_run:
                self.logger.info("Inside the while loop, should_run is True.")
                time.sleep(interval)
                pyautogui.move(100, 0, duration=0.2)
                pyautogui.move(-100, 0, duration=0.2)
                if self.callback:
                    self.callback("Mouse moved.")
        except Exception as e:
            self.logger.error(f"An error occurred while moving the mouse: {e}")

    def stop_moving(self):
        self.should_run = False
        if self.caffeinate_process:
            self.caffeinate_process.terminate()