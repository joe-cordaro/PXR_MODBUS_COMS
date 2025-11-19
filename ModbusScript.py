
from pymodbus.client import ModbusTcpClient

# Configuration
IP_ADDRESS = "192.168.2.1"
PORT = 502  # Default Modbus TCP port
UNIT_ID = 1  # Slave ID (often 1 for single device)
REGISTER_ADDRESS = 100  # Example register address
REGISTER_COUNT = 2  # Number of registers to read

def read_modbus_data():
    # Create Modbus TCP client
    client = ModbusTcpClient(IP_ADDRESS, port=PORT)
    
    # Connect to the server
    if client.connect():
        print(f"Connected to Modbus server at {IP_ADDRESS}")
        
        # Read holding registers
        response = client.read_holding_registers(REGISTER_ADDRESS, REGISTER_COUNT, unit=UNIT_ID)
        
        if not response.isError():
            print(f"Telemetry Data: {response.registers}")
        else:
            print(f"Error reading registers: {response}")
        
        # Close connection
        client.close()
    else:
        print(f"Failed to connect to {IP_ADDRESS}")

if __name__ == "__main__":
    read_modbus_data()
