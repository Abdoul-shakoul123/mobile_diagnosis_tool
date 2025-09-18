# modules/device_info.py
import subprocess

class DeviceInfo:
    def __init__(self):
        pass

    def get_device_info(self):
        try:
            # Angalia kama device ipo
            result = subprocess.check_output(["adb", "devices"]).decode()
            if "device" not in result.splitlines()[1]:
                return {
                    "brand": "No device",
                    "model": "N/A",
                    "os": "N/A",
                    "battery": "N/A"
                }

            # Soma brand
            brand = subprocess.check_output(["adb", "shell", "getprop", "ro.product.brand"]).decode().strip()
            model = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode().strip()
            os_version = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode().strip()
            battery = subprocess.check_output(["adb", "shell", "dumpsys", "battery"]).decode()

            # Tafuta battery level
            level = "Unknown"
            for line in battery.splitlines():
                if "level:" in line:
                    level = line.split(":")[1].strip()
                    break

            return {
                "brand": brand,
                "model": model,
                "os": os_version,
                "battery": f"{level}%"
            }

        except Exception as e:
            return {
                "brand": "Error",
                "model": "Error",
                "os": "Error",
                "battery": str(e)
            }
