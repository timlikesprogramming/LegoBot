#include <Servo.h>

Servo servo1; // Servo for '1'
Servo servo2; // Servo for '2'

// Define initial positions for the servos
int pos1 = 90; // Initial position for servo 1
int pos2 = 90; // Initial position for servo 2

void setup() {
  servo1.attach(9);  // Connect first servo to pin 9
  servo2.attach(10); // Connect second servo to pin 10

  servo1.write(pos1);
  servo2.write(pos2);
  Serial.begin(9600); // Start the Serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read the entire line from Serial
    String servoID = command.substring(0, 1); // Get the servo identifier
    int stepSize = command.substring(1).toInt(); // Extract the step size (rest of the command)

    // Adjust the corresponding servo based on the identifier
    if (servoID == "1") {
      pos1 = constrain(pos1 + stepSize, 0, 180); // Update position with step size
      servo1.write(pos1);
    } else if (servoID == "2") {
      pos2 = constrain(pos2 + stepSize, 0, 180); // Update position with step size
      servo2.write(pos2);
    }
  }
}