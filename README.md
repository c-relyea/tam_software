# tam_software

Software for the TAM (Tracheal Acoustic Monitor) wearable device.

## Receiver

Runs on macOS or Raspberry Pi. Connects to a TAM board over BLE and prints IMU, SpO2, and battery data.

```bash
cd receiver
pip install -r requirements.txt
python receive.py
```

## BLE

| Advertisement | Name | Description |
|---|---|---|
| LE Audio (Auracast) | `TAMAUDIO` | Stereo LC3 audio broadcast — connect with any Auracast receiver |
| GATT peripheral | `TAMDATA` | Sensor data over Nordic UART Service |
