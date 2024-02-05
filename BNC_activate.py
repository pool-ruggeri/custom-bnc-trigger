import serial
import time

# Connect to Arduino's serial port - check on Device manager the COM port number
arduino = serial.Serial('COM5', 9600)
time.sleep(20)  # Wait for the connection to establish


# Function to activate pin 2
def activate_pin():
    arduino.write(b'ACTIVATE\n')
    print("Pin 2 activated.")


# Function to deactivate pin 2
def deactivate_pin():
    arduino.write(b'DEACTIVATE\n')
    print("Pin 2 deactivated.")


# Example usage
activate_pin()
time.sleep(5)  # Keep the pin active for 5 seconds
deactivate_pin()

arduino.close()  # Close the serial connection
