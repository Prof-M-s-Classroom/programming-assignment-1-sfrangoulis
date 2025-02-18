import serial
import time
from temperature import Temperature
from stack import CircularStack

# Define serial connection parameters
COM_PORT = 'COM2'  # Update based on your system
BAUD_RATE = 9600


def read_from_arduino(serial_connection, stack):
    """
    Reads data from Arduino and stores it in the CircularStack.
    """
    try:
        if serial_connection.in_waiting > 0:
            data = serial_connection.readline().decode('utf-8').strip()

            if "Temperature" in data:  # Example: "Temperature: 25.6°C, Humidity: 46.0%"
                parts = data.split(", ")
                temp_value = float(parts[0].split(": ")[1][:-2])  # Extract temperature
                humidity_value = float(parts[1].split(": ")[1][:-1])  # Extract humidity

                # Create Temperature object and push to stack
                temp_obj = Temperature(temp_value, humidity_value)
                stack.push(temp_obj)

                # Call print_stack to display the latest five readings
                print("\nLatest 5 Readings:")
                stack.print_stack()

    except Exception as e:
        print(f"Error reading from Arduino: {e}")


def main():
    # Initialize serial connection
    try:
        arduino = serial.Serial(COM_PORT, BAUD_RATE, timeout=2)
        time.sleep(2)  # Allow time for the connection to establish
        print("Connected to Arduino. Reading DHT11 data...\n")

        # Initialize circular stack
        temp_stack = CircularStack()

        while True:
            read_from_arduino(arduino, temp_stack)
            time.sleep(2)  # Wait before next reading

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        if 'arduino' in locals():
            arduino.close()


if __name__ == "__main__":
    main()