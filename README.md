# custom-bnc-trigger

## BNC Connector with Arduino MEGA and Python

# Overview

This README provides instructions on how to use a BNC connector with an Arduino MEGA, controlled by Python scripts. The BNC connector has its ground connected to the GND pin of the Arduino and the other end connected to pin 2 of the digital pins.

# Components
Arduino MEGA <br />
BNC Connector <br />
Python Scripts: BNC_activate.py, BNC_activate_countdown.py
Arduino Sketch: BNC_sketch/BNC_sketch_v1.ino
Wiring

Connect the ground (GND) of the BNC connector to the GND pin of the Arduino MEGA.
Connect the signal wire of the BNC connector to pin 2 of the Arduino MEGA's digital pins.

# BNC_activate.py
The BNC_activate.py script is designed to activate pin 2 on the Arduino MEGA. This script can be used to test the connection and functionality of the BNC connector.

# BNC_activate_countdown.py
The BNC_activate_countdown.py script is specifically created to work with BIOPAC AcqKnowledge software. In this software, the acquisition starts upon receipt of positive edges of external triggers (refer to the BIOPAC manual, Chapter 8 for more details). The functionality of this script is similar to BNC_activate.py, but with an added visual countdown. This countdown allows the user to prepare and acknowledge that they are ready to listen for the trigger. This can be crucial in scenarios where precise timing is required.

# Arduino Sketch (BNC_sketch_v1.ino)
The BNC_sketch_v1.ino file is intended for use with the Arduino IDE. It is used to load the necessary firmware onto the Arduino MEGA to enable communication with the BNC connector and control of pin 2. Note that when pin 2 is activated, the integrated LED is also activated.

# Usage
Connect the BNC connector as described in the "Wiring" section above.
Upload the BNC_sketch_v1.ino sketch to your Arduino MEGA using the Arduino IDE.
Run either BNC_activate.py or BNC_activate_countdown.py from your Python environment to control the BNC connector and Arduino.
