# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "adafruit-blinka",
#     "adafruit-circuitpython-ahtx0",
#     "adafruit-circuitpython-vcnl4200",
#     "rpi.gpio",   
# ]
# ///
"""
Lecture combinée AHT20 et VCNL4200 sur le même bus I2C
Cours 243-413-SH, Semaine 3
"""

import board
import adafruit_ahtx0
import adafruit_vcnl4200

i2c = board.I2C()

aht20 = adafruit_ahtx0.AHTx0(i2c)
vcnl = adafruit_vcnl4200.Adafruit_VCNL4200(i2c)

print("=== Station IoT Multi-Capteurs ===")
print("Capteurs sur le bus I2C :")
print("  - AHT20 (0x38) : temperature, humidite")
print("  - VCNL4200 (0x51) : proximite, lumiere")
print()

print("--- Données environnementales (AHT20) ---")
print(f"Temperature : {aht20.temperature:.1f} C")
print(f"Humidite    : {aht20.relative_humidity:.1f} %")
print()

print("--- Donnees spatiales (VCNL4200) ---")
print(f"Proximite   : {vcnl.proximity}")
print(f"Lumiere     : {vcnl.lux:.1f} lux")
print()

if vcnl.proximity > 100:
    print("Objet détecté à proximité!")
if vcnl.lux < 50:
    print("Faible éclairage ambiant")

print("\n=== Terminé ===")