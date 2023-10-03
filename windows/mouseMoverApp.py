from tkinter import Tk, Label, Button, Text, END
from mouseMover import MouseMover
import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

# Initialize logging
logging.basicConfig(
    filename='mouse_mover.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.logger = logging.getLogger('MouseMoverApp')
        root.title("Mouse Mover")
        
        self.label = Label(root, text="Mouse Mover is Stopped")
        self.label.pack()

        self.runtime_label = Label(root, text="Runtime: 0h 0m 0s")
        self.runtime_label.pack()

        self.start_button = Button(root, text="Start", command=self.start_moving)
        self.start_button.pack()

        self.stop_button = Button(root, text="Stop", command=self.stop_moving)
        self.stop_button.pack()

        self.text_box = Text(root, height=5, width=40)
        self.text_box.pack()

        self.mouse_mover = MouseMover(callback=self.add_event)
        self.event_queue = []
        self.start_time = None

    def update_runtime(self):
        self.logger.info("Inside update_runtime.")
        if self.start_time is not None:
            elapsed_time = int(time.time() - self.start_time)
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.runtime_label.config(text=f"Runtime: {hours}h {minutes}m {seconds}s")
            self.root.after(1000, self.update_runtime)

    def add_event(self, event):
        self.logger.info(f"Event added: {event}")
        self.event_queue.append(event)
        if len(self.event_queue) > 5:
            self.event_queue.pop(0)
        self.text_box.delete(1.0, END)
        for event in self.event_queue:
            self.text_box.insert(END, event + '\n')


    def start_moving(self):
        try:
            self.logger.info("MouseMoverApp: start_moving called")
            self.start_time = time.time()
            self.update_runtime()
            self.label.config(text="Mouse Mover is Running")
            self.add_event("Mouse Mover started.")
            self.thread = threading.Thread(target=self.mouse_mover.start_moving)
            self.thread.daemon = True
            self.thread.start()
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            self.add_event(f"An error occurred: {e}")

    def stop_moving(self):
        try:
            self.logger.info("MouseMoverApp: stop_moving called")
            self.mouse_mover.stop_moving()
            self.label.config(text="Mouse Mover is Stopped")
            self.add_event("Mouse Mover stopped.")
            self.start_time = None
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            self.add_event(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    try:
        root = Tk()
        app = MouseMoverApp(root)
        root.mainloop()
    except Exception as e:
        logging.error(f"An error occurred while running the application: {e}")