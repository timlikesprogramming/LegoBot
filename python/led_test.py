import time
import serial

def send_input_to_arduino(ser, input_data):
    input_data_with_newline = input_data + '\n'  # Add newline to the input
    ser.write(input_data_with_newline.encode())  # Encode the string to bytes and send it to Arduino
    print(f"Sent to Arduino: {input_data_with_newline.strip()}")
    time.sleep(0.1)  # Small delay to ensure data transfer

    # Read and print the Arduino response, if any
    while ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
        print(f"Arduino says: {response}")

def main():
    # Set up the serial connection (adjust the port as necessary)
    # For Unix-like systems like Linux or macOS
    port = '/dev/arduino'
    baud_rate = 9600
    timeout = 1  # Timeout in seconds

    try:
        with serial.Serial(port, baud_rate, timeout=timeout) as ser:
            
            # Check initial messages from Arduino
            while ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                print(f"Arduino says: {response}")

            while True:
                user_input = input("Type 'on' to turn ON the LED, 'off' to turn OFF the LED:").strip()
                if user_input.lower() in ['on', 'off']:
                    send_input_to_arduino(ser, user_input)
                else:
                    print("Invalid input. Please type 'on' to turn ON the LED, 'off' to turn OFF the LED.")
    except serial.SerialException as e:
        print(f"Error initializing serial connection: {e}")
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()