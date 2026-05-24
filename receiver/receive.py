"""
TAM BLE Receiver
Connects to a TAM board advertising as TAMDATA and prints
sensor data (IMU, SpO2, battery) from the Nordic UART Service.

Usage:
    python receive.py

Requirements:
    pip install -r requirements.txt
"""

import asyncio
from bleak import BleakScanner, BleakClient

DEVICE_NAME = "TAMDATA"

# Nordic UART Service UUIDs
NUS_TX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # device → host (notify)
NUS_RX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"  # host → device (write)


def on_data(sender, data: bytearray):
    line = data.decode("utf-8", errors="replace").strip()
    if line.startswith("A:"):
        # IMU: "A:ax,ay,az G:gx,gy,gz"
        print(f"[IMU]     {line}")
    elif line.startswith("P:"):
        # PPG: "P:red,ir,green"
        print(f"[SpO2]    {line}")
    elif line.startswith("B:"):
        # Battery: "B:79%"
        print(f"[Battery] {line}")
    else:
        print(f"[?]       {line}")


async def main():
    print(f"Scanning for {DEVICE_NAME}...")
    device = await BleakScanner.find_device_by_name(DEVICE_NAME, timeout=15)

    if device is None:
        print(f"Could not find {DEVICE_NAME}. Is it powered on and advertising?")
        return

    print(f"Found {device.name} — connecting...")

    async with BleakClient(device) as client:
        print(f"Connected. Listening for sensor data (Ctrl+C to stop)...\n")
        await client.start_notify(NUS_TX_UUID, on_data)

        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            pass

    print("Disconnected.")


if __name__ == "__main__":
    asyncio.run(main())
