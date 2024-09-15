import serial
import logging

logging.basicConfig(level=logging.DEBUG)

arduino_port = '/dev/arduino'  # Update this with your actual port
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port, baud_rate)
    print("Serial port opened successfully")
    ser.close()
except serial.SerialException as e:
    logging.error(f"Error opening serial port: {e}")