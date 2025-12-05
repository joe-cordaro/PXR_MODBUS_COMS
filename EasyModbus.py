
import asyncio
from pymodbus.client import AsyncModbusTcpClient
from pymodbus.client import ModbusTcpClient
from pymodbus.framer import FramerType

unit_id = 1
reg_address = 3999
IP_address = "192.168.2.1"

async def main():
    client = AsyncModbusTcpClient(host = IP_address, port=502, framer=FramerType.RTU)

    await client.connect()
    if not client.connected:
        print(" Could not connect to gateway.")
        return
    else:
     print("Connected to 192.168.2.1")

    rr = await client.read_holding_registers(
        address=reg_address,
        count=1,
        unit=unit_id
    )
    if rr.isError():
        print(f"❌ Modbus error: {rr}")
    else:
        print(f"📗 Register 4000 value: {rr.registers[0]}")

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())



