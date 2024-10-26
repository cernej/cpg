def levensteinova_vzdalenost(dotaz1, dotaz2):
    """
    Levensteinova vzdalenost říka, jak jsou 2 řetězce rozdílné, pokud jsou stejné je Levensteinova vzdalenost 0,
    pro řetězce "čas" a "čaj" je Levensteinova vzdalenost 1 (liší se v 1 písmenu)
    """
    i = 0
    lenght = min(len(dotaz1), len(dotaz2))
    levenstein = 0
    while i < lenght:
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
        i += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein


def levensteinova_vzdalenost_for(dotaz1, dotaz2):
    levenstein = 0
    for pismeno1, pismeno2 in zip(dotaz1, dotaz2):
        if pismeno1 != pismeno2:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print(levensteinova_vzdalenost_for(query1, query2))
    print(levensteinova_vzdalenost_for(query2, query3))
    print(levensteinova_vzdalenost_for(query1, query3))
    print(levensteinova_vzdalenost_for(query1, query4))