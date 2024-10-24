import argparse
from cryptography.fernet import Fernet

beskrivning = "Generera en nyckel för att cryptera data med ett annat program"
parser = argparse.ArgumentParser(description=beskrivning)

parser.add_argument("filnamn", help="Namnet på filen där du vill spara nyckeln (skriver över allt i den filen)")

args = parser.parse_args()

# Hade kunnat lägga till en if fil exist grej, men tycker det funkar bra att det skapas en ny fil 

nyckel = Fernet.generate_key()

with open (args.filnamn, "wb") as fil:
    fil.write(nyckel)
print(f"Nyckeln har sparats i {args.filnamn}")