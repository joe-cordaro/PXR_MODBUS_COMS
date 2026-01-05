# Source - https://stackoverflow.com/q
# Posted by joeyda3rd
# Retrieved 2025-12-16, License - CC BY-SA 4.0

import time
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusIOException

def run():
        print("Creating client")
        client = ModbusSerialClient("/dev/ttyUSB0", method='rtu', baudrate=9600, stopbits=1, parity='N', bytesize=8, timeout=1)

        print("Connecting to client")
        if not client.connect():
                print("Failed to connect to client")
                return

        # List of register addresses to read from
        register_addresses = [0x0001, 0x0002, 0x0003, 0x0004, 0x0005, 0x0010, 0x0011, 0x0012, 0x0013, 0x0030, 0x0031, 0x0020, 0x0021, 0x0022, 0x0023, 0x9999]

        # Read from each register
        for address in register_addresses:
                try:
                        response = client.read_holding_registers(address, count=1, device_id=1)
                        if response.isError():
                                print(f"Error reading register {address}: {response}")
                        else:
                                print(f"Register {address}: {response.registers}")
                        time.sleep(0.035)
                except ModbusIOException as e:
                        print(f"Modbus IO Exception reading register {address}: {e}")

        print("Closing client")
        client.close()

run()
