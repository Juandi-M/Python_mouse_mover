# Mouse Mover for macOS 🖱️

## Description 📝

Tired of your Mac going to sleep when you don't want it to? Mouse Mover is a simple Python application that simulates mouse movement to prevent your Mac from going to sleep. It comes with a neat GUI so you can easily start and stop the mouse movement. Plus, it shows you how long the program has been running and logs important events.

## Features 🌟

- Simple and intuitive GUI.
- Logs the last 5 events.
- Shows runtime in hours, minutes, and seconds.
- Uses Python's threading to ensure smooth operation.

## Prerequisites 📋

- Python 3.x
- Tkinter
- pyautogui

## Installation 🛠️

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Python_mouse_mover.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Python_mouse_mover
   ```

3. Install the required packages:

   ```bash
   pip3 install -r requirements.txt
   ```

## Usage 🖥️

### To run the script:

1. Navigate to the `src` folder:

   ```bash
   cd src
   ```

2. Run the Python script:

   ```bash
   python3 MouseMoverApp.py
   ```

### To create a standalone macOS application:

1. Navigate to the project root directory.
2. Run the setup script:

   ```bash
   python3 setup.py py2app
   ```

3. Find the standalone application in the `dist` directory.

## Contributing 🤝

Feel free to fork the project, open a PR, or submit an issue.

## License 📄

This project is licensed under the GNU GENERAL PUBLIC LICENSE
