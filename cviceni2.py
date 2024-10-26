def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def faktorial_for(n):
    vysledek = 1
    for x in range(1, n + 1):
        vysledek *= x
    return vysledek

def faktorial_while(n):
    vysledek = 1
    while n > 1:
        vysledek *= n
        n -= 1
    return vysledek

if __name__ == "__main__":
    
    print(faktorial(10))
    print(faktorial_for(10))
    print(faktorial_while(10))


    
    