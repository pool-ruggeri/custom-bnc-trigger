// Define the pin for the BNC cable connection
const int bncPin = 2;
const int ledPin = LED_BUILTIN; // Built-in LED pin

void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud rate
  pinMode(bncPin, OUTPUT); // Set the BNC cable pin as an output
  pinMode(ledPin, OUTPUT); // Set the LED pin as an output
  digitalWrite(bncPin, LOW); // Ensure BNC pin starts LOW (off)
  digitalWrite(ledPin, LOW); // Ensure LED starts LOW (off)
}

void loop() {
  if (Serial.available() > 0) { // Check if there's incoming serial data
    String command = Serial.readStringUntil('\n'); // Read the incoming data until newline
    // Check if the command is to activate pin 2
    if (command == "ACTIVATE") {
      digitalWrite(bncPin, HIGH); // Activate the BNC pin
      digitalWrite(ledPin, HIGH); // Turn on the LED
      Serial.println("Pin 2 Activated"); // Send confirmation back to PC
    } else if (command == "DEACTIVATE") {
      digitalWrite(bncPin, LOW); // Deactivate the BNC pin
      digitalWrite(ledPin, LOW); // Turn off the LED
      Serial.println("Pin 2 Deactivated"); // Send confirmation back to PC
    }
  }
}
