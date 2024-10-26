# funkce vrati treti plozku ze seznamu pokud existuje napr [0,9,8,7] -> 8 
# pokud neexistuje, vrati None
def vrat_treti(seznam):
    if len(seznam) < 3:
        return None
    else:
        return seznam[2]

# funkce vypocte prumer za pomoci funkci sum() / len()
def udelej_prumer(cisla):
    return sum(cisla) / len(cisla)

# funkce bere jako parametr slovnik student a vypise jeho jmeno a prumer znamek
def naformatuj_text(student):
    print(f"Jmeno: {student["jmeno"]}, prumer znamek: {round(udelej_prumer(student["znamky"]), 2)}")

if __name__ == "__main__":
    # polozky = [1,2,10,15]
    # vysledek = vrat_treti(polozky)
    # print(vysledek)

    # seznam_cisel = [1,2,3,4,5]
    # prumer = udelej_prumer(seznam_cisel)
    # print(prumer)

    data = {
        "jmeno": "Bob",
        "znamky": [1,2,1,1,2,3]
    }
    naformatuj_text(data)