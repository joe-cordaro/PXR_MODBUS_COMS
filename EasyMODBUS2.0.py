
from pymodbus.client import ModbusTcpClient
from pymodbus.framer import FramerType

IP_Address = "172.22.17.254" #"192.168.2.1"
Port = 502 #Com2, Com1 is 26501
Framer = FramerType.RTU
C = 32
UnitID = 5
RegAddress = 1016


def read_RTU_over_TCP():

# Connection to TCP/IP
    client = ModbusTcpClient(
        host = IP_Address, 
        port = Port,
        framer = Framer, 
        timeout= 3
    ) 
    
    connected = client.connect()
    if not connected:
        print("Failed to connect to Gateway")
        return
    print(f"Connected to Gateway on {IP_Address}:{Port}")

#Read register over Framer
    try:
        rr = client.read_holding_registers(
            address=RegAddress,
            count= C,
            device_id=UnitID, 
            no_response_expected = False #False expects a response
        )
        if rr.isError():
            print(f"Modbus error: {rr}")
        else:
            value = rr.registers[0]
            print(f"Register {RegAddress} value: {rr.registers[0]}")  
    except Exception as e:
        print(f"Runtime error: {e}")
    
    finally:
        client.close()
        print("Connection closed.")

if __name__ == "__main__":
    read_RTU_over_TCP()
