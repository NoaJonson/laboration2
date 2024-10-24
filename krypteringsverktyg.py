import argparse
from pathlib import Path
from cryptography.fernet import Fernet

beskrivning = "Detta verktyg används för att kryptera och dekryptera filer med hjälp av en symmetrisk nyckel. Användare kan ange en fil och en nyckel, samt välja om de vill kryptera eller dekryptera filen."
parser = argparse.ArgumentParser(description=beskrivning)

parser.add_argument("nyckelfil", help="Sökvägen till filen som innehåller krypteringsnyckeln. Nyckeln måste vara i formatet som genereras av Fernet.")
parser.add_argument("fil", help="Sökvägen till den fil som ska krypteras eller dekrypteras. Filens innehåll kommer att skrivas över med den krypterade eller dekrypterade versionen.")
parser.add_argument("funktion", choices=("kryptera", "dekryptera"), help= "Välj vilken åtgärd som ska utföras: 'kryptera' för att kryptera filen, 'dekryptera' för att återställa filen till dess ursprungliga innehåll.")

args = parser.parse_args()


fil_sökväg = Path(args.fil)
nyckelfil_sökväg = Path(args.nyckelfil)


if not fil_sökväg.exists() and not nyckelfil_sökväg.exists():
    print(f"Varken {args.fil} eller {args.nyckelfil} finns på detta system")
    exit()
elif not fil_sökväg.exists():
    print(f"{args.fil} finns inte på detta system")
    exit()
elif not nyckelfil_sökväg.exists():
    print(f"{args.nyckelfil} finns inte på detta systemm")
    exit()


with open (nyckelfil_sökväg) as fil:
    nyckel = fil.read()

cipher_suite = Fernet(nyckel)

with open (fil_sökväg) as fil:
    filtext = fil.read()


if args.funktion == "kryptera":

    inputtext = f"{filtext}".encode() #encode bara för att göra till binärt tror jag

    cipher_text = cipher_suite.encrypt(inputtext)

    with open (fil_sökväg, "wb") as fil:
        fil.write(cipher_text)
    print(f"{args.fil} har krypterats")

else:

    decodad_text = cipher_suite.decrypt(filtext)

    with open (fil_sökväg, "wb") as fil:
        fil.write(decodad_text)
    print(f"{args.fil} har dekrypterats")