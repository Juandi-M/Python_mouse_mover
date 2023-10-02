import pyautogui
import time
import logging

class MouseMover:
    def __init__(self, callback=None):
        self.should_run = True
        self.callback = callback
        self.logger = logging.getLogger('MouseMover')

    def start_moving(self):
        try:
            interval = 5  # 5 seconds
            while self.should_run:
                time.sleep(interval)
                pyautogui.move(1, 0, duration=0.2)
                pyautogui.move(-1, 0, duration=0.2)
                if self.callback:
                    self.callback("Mouse moved.")
        except Exception as e:
            self.logger.error(f"An error occurred while moving the mouse: {e}")

    def stop_moving(self):
        self.should_run = False
