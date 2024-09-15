import serial
import time
import keyboard


def main():
    # Set up the serial connection (make sure to change 'COM3' to your Arduino's port)
    arduino_port = '/dev/ttyS3'  # In WSL this COM4 is equivalent to /dev/ttyS3
    baud_rate = 9600
    ser = serial.Serial(arduino_port, baud_rate)
    time.sleep(2)  # Wait for the serial connection to initialize

    step_size = 1  # Set the step size
    print("Press and hold 'a' to move Servo 1 clockwise")
    print("Press and hold 's' to move Servo 1 counterclockwise")
    print("Press and hold 'k' to move Servo 2 clockwise")
    print("Press and hold 'l' to move Servo 2 counterclockwise")
    print("Press 'q' to quit the program")

    try:
        while True:
            # Check the state of each key
            if keyboard.is_pressed('a'):  # Move Servo 1 clockwise
                command = f"1{step_size}\n"
                ser.write(command.encode())  # Send command to Arduino
                print(f"Sent command: {command.strip()}")
                time.sleep(
                    0.01)  # Adjust this value to control the speed of movement

            elif keyboard.is_pressed('s'):  # Move Servo 1 counterclockwise
                command = f"1{-step_size}\n"
                ser.write(command.encode())  # Send command to Arduino
                print(f"Sent command: {command.strip()}")
                time.sleep(
                    0.01)  # Adjust this value to control the speed of movement

            elif keyboard.is_pressed('k'):  # Move Servo 2 clockwise
                command = f"2{step_size}\n"
                ser.write(command.encode())  # Send command to Arduino
                print(f"Sent command: {command.strip()}")
                time.sleep(
                    0.01)  # Adjust this value to control the speed of movement

            elif keyboard.is_pressed('l'):  # Move Servo 2 counterclockwise
                command = f"2{-step_size}\n"
                ser.write(command.encode())  # Send command to Arduino
                print(f"Sent command: {command.strip()}")
                time.sleep(
                    0.01)  # Adjust this value to control the speed of movement

            # Quit the program
            if keyboard.is_pressed('q'):
                print("Quitting program.")
                break

            time.sleep(0.01)  # Add a small delay to prevent high CPU usage

    except KeyboardInterrupt:
        print("Program interrupted. Exiting...")

    # Close the serial connection
    ser.close()


if __name__ == '__main__':
    main()
