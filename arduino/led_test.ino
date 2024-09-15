const int ledPin = LED_BUILTIN;  // Typically the built-in LED is on pin 13

void setup() {
  // Initialize the built-in LED as an output
  pinMode(ledPin, OUTPUT);
  // Initialize Serial communication at 9600 bits per second
  Serial.begin(9600);
}

void loop() {
  static String inputString = "";  // a string to hold incoming data
  if (Serial.available() > 0) {    // Check if there is any data available to read
    char incomingByte = Serial.read();
    
    if (incomingByte == '\n') {
      // Process the input string
      if (inputString.equalsIgnoreCase("on")) {
        digitalWrite(ledPin, HIGH);
        Serial.println("LED turned ON");
      } else if (inputString.equalsIgnoreCase("off")) {
        digitalWrite(ledPin, LOW);
        Serial.println("LED turned OFF");
      }

      // Clear the input string after processing
      inputString = "";
    } else {
      // Add the incoming byte to the input string
      inputString += incomingByte;
    }
  }
}