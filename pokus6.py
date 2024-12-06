class BankovniUcet:
    def __init__(self, zustatek):
        self.nazev = "aaa"
        self.__zustatek = zustatek
    
    @property
    def zustatek(self):
        return self.__zustatek
    
    @zustatek.setter
    def zustatek(self, novy_zustatek):
        if novy_zustatek < 0:
            raise ValueError("Zustatek nemuze byt zaporny")
        self.__zustatek = novy_zustatek
    

if __name__ == "__main__":
    bu = BankovniUcet(100)
    print(bu.zustatek)
    bu.zustatek = 200
    print(bu.zustatek)