import serial
import time

# Replace 'COM3' with the correct port for your system
arduino_port = 'COM3'
baud_rate = 9600

try:
    # Establish connection with Arduino
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Allow time for connection to establish
    print("Connected to Arduino. Reading Ultrasonic Sensor data...")

    while True:
        if arduino.in_waiting > 0:
            distance = arduino.readline().decode('utf-8').strip()
            if distance:
                print(f"Distance: {distance} cm")
        time.sleep(2)  # Read every 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
    arduino.close()

except serial.SerialException:
    print("Error: Could not connect to Arduino. Check your port and connection.")
