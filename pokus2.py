import sys

def main(jmeno_souboru):
    soubor = open(jmeno_souboru, "r")
    for radek in soubor:
        polozky = radek.split(",")
        vek = int(polozky[1])
        if vek >= 20:
            print(radek)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Zadej jmeno souboru")
        sys.exit(1)
    main(sys.argv[1])