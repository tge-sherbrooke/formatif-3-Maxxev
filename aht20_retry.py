# /// script
# requires-python = ">=3.9"
# dependencies = [
#    "adafruit-blinka",
#    "adafruit-circuitpython-ahtx0",
#    "rpi.gpio",
# ]
# ///
"""
Lecture du capteur AHT20 avec pattern de retry
Cohérent avec le pattern DHT22 de la semaine 2
Cours 243-413-SH, Semaine 3
"""

import board
import adafruit_ahtx0
import time

# Constantes de retry (même que semaine 2)
MAX_TENTATIVES = 3
DELAI_RETRY = 1 # seconde

def lire_avec_retry():
    """
    Lit l'AHT20 avec plusieurs tentatives.
    Pattern identique au DHT22 de la semaine 2.
    """
    # Initialiser le bus I2C
    i2c = board.I2C()
    
    for tentative in range(MAX_TENTATIVES):
        try:
            # Créer l'objet capteur
            capteur = adafruit_ahtx0.AHTx0(i2c)

            # Lire les valeurs
            temperature = capteur.temperature
            humidite = capteur.relative_humidity
            
            # Vérifier que les valeurs sont valides
            if temperature is not None and humidite is not None:
                return {
                    "temperature": round(temperature, 1),
                    "humidite": round(humidite, 1),
                    "valide": True
                }
                
        except Exception as e:
            print(f"  Tentative {tentative + 1}/{MAX_TENTATIVES} : {e}")
            time.sleep(DELAI_RETRY)
    
    # Échec après toutes les tentatives  
    return {
        "temperature": None,
        "Humidite": None,
        "valide": False
    }

if __name__ == "__main__":
    print("=== Lecture AHT20 avec retry ===")
    print(f"Maximum tentatives : {MAX_TENTATIVES}")
    print(f"Délai entre tentatives : {DELAI_RETRY} s")
    print()
    
    # Lecture avec retry
    donnees = lire_avec_retry()
    
    if donnees["valide"]:
        print(f"Temperature : {donnees["temperature"]} C")
        print(f"Humidite    : {donnees["humidite"]} %")
    else:
        print("ERREUR : Échec lecture après plusieurs tentatives")
        print("Verifiez :")
        print(" 1. Le cablage (STEMMA QT ou fils)")
        print(" 2. L'alimentation (3.3V)")
        print(" 3. La detection (sudo i2cdetect -y 1 -> 0x38)")

    print("\n=== Termine ===")