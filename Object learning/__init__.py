class Polonez():   
    
    def __init__(self , kolor):
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.spalanie_na_100 = 12
        print('Polonez jest cool')
        self.zasieg()
    
    def zasieg(self):
        zasieg = self.ilosc_paliwa * 100 / self.spalanie_na_100
        return zasieg
 
        
polonez = Polonez('czerwony') # <- funkcja __init__ uruchamiana jest pierwsza poprzez przypisanie instancji(polonez,polonez1)do klasy
polonez.ilosc_paliwa += 10
polonez1 = Polonez('zielony')

print(int(polonez.zasieg()))
print(int(polonez1.zasieg()))