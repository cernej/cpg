class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        print(f'Zvire {self.jmeno} bylo vytvoreno')

class Pes(Zvire):
    def __init__(self, jmeno, rasa):
        super().__init__(jmeno)
        self.rasa = rasa
        print(f'Pes rasy {self.rasa} byl vytvoren')
    
    # {"zvire": {"jmeno": "abc", "rasa": "xxx"}}
    @classmethod
    def parse(cls, data):
        jmeno = data.get("zvire", {}).get("jmeno")
        rasa = data.get("zvire", {}).get("rasa")
        return cls(jmeno, rasa)

if __name__ == "__main__":
    pes = Pes("Alik", "jezevcik")
    pes.jmeno

    data = {"zvire": {"jmeno": "abc", "rasa": "xxx"}}
    pes2 = Pes.parse(data)
    print(pes2.jmeno)