class Polonez():
    
        
    def hamuj(self):
        print('hamuje')
        
    def skrecaj(self , strona):
        print(f'skrecaj w {strona}')
    
    def ilosc_paliwa(self):
        return print('10 litrow')  
    
    def dodaj(self , a , b):
        return print(a + b)
    
    def __str__(self):
        return 'Adamo'
    
    
#funkcje ktore wykorzystuja instancje klasy , zakomentowane te ktora sa podowane przez __init__
polonez = Polonez() # <- funkcja __init__ uruchamiana jest pierwsza poprzez przypisanie instancji(polonez_adama)do klasy
print(polonez)  # <- funkcja __str__ daje bezposredni dostep do instancji(polonez_adama)



#typy
   

#funkcje wywolywane podstawowo
polonez.hamuj()
polonez.skrecaj('prawo')
ilosc_paliwa = polonez.ilosc_paliwa()
print(ilosc_paliwa)
print(polonez.dodaj(2,2))

# funkacja ktora bezposrednio jest wykonywana bez klasy
def hamuj():
    print('hamuje1')

hamuj()