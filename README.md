# tam_software

Software for the TAM (Tracheal Acoustic Monitor) wearable device.

## Structure

| Folder | Description |
|---|---|
| `firmware/` | nRF5340 application — LE Audio Auracast broadcast source + BLE sensor data |
| `hardware/` | Board definition files for the TAM board (Zephyr/NCS) |
| `receiver/` | Python BLE receiver — connects to TAM and logs sensor data |

## Firmware

Built with Nordic NCS v2.8.0. See `firmware/README.md` for build and flash instructions.

```bash
west build -b tam_board/nrf5340/cpuapp --sysbuild -- -DCONFIG_AUDIO_DEV=2
west flash --runner jlink
```

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
