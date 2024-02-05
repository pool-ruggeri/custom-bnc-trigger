import serial
import time
import tkinter as tk
from threading import Thread

# Initialize the serial connection (adjust the port for your environment)
arduino = serial.Serial('COM5', 9600, timeout=1)

def activate_pin():
    """Function to activate pin 2."""
    arduino.write(b'ACTIVATE\n')
    print("Pin 2 activated.")

def deactivate_pin():
    """Function to deactivate pin 2."""
    arduino.write(b'DEACTIVATE\n')
    print("Pin 2 deactivated.")

def show_prompt():
    """Display the GUI prompt."""
    root = tk.Tk()
    root.title("Serial Connection Status")
    message = "Serial connection established, you have 20 seconds to click on \"Demarrer\" on Acqknowledge."
    label = tk.Label(root, text=message, width=100, height=10)
    label.pack()
    # Close the window after 20 seconds
    root.after(20000, root.destroy)
    root.mainloop()

def countdown_and_activate():
    """Countdown 20 seconds and activate pin 2."""
    time.sleep(20)  # Wait for 20 seconds
    activate_pin()
    # Optional: wait for 5 seconds then deactivate pin 2
    time.sleep(5)
    deactivate_pin()
    arduino.close()  # Close the serial connection

# Run the GUI in a separate thread
Thread(target=show_prompt).start()

# Start the countdown and activate pin 2
countdown_and_activate()
