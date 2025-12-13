class People:
    def blyat(self, jopa):
        for i in range(4):
            print(f'{jopa} Blyat')

    def suka(self):
        jopa = "опа"
        self.blyat(jopa)

vasya = People()

if __name__ == "__main__":
    vasya.suka()