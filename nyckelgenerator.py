import argparse
from cryptography.fernet import Fernet

beskrivning = "bla bla bla"
parser = argparse.ArgumentParser(description=beskrivning)

parser.add_argument("filnamn", help="bla bla bla")

args = parser.parse_args()

# Hade kunnat lägga till en if fil exist grej, men tycker det funkar bra att det skapas en ny fil 

nyckel = Fernet.generate_key()

with open (args.filnamn, "wb") as fil:
    fil.write(nyckel)
print(f"Nyckeln har sparats i {args.filnamn}")