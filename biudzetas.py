import pickle
from models.islaidu_irasas import IslaiduIrasas
from models.pajamu_irasas import PajamuIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_faila()

    def nuskaityti_faila(self):
        try:
            with open("biudzeto_zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_faila(self):
        with open("biudzeto_zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self):
        suma = abs(float(input("Suma: ")))
        siuntejas = input("Siuntėjas: ")
        info = input("Papildoma informacija: ")
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_faila()

    def prideti_islaidu_irasa(self):
        suma = abs(float(input("Suma: ")))
        atsiskaitymas = input("Atsiskaitymo būdas: ")
        isigyta = input("Įsigyta prekė/paslauga: ")
        irasas = IslaiduIrasas(suma, atsiskaitymas, isigyta)
        self.zurnalas.append(irasas)
        self.irasyti_faila()

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            if type(irasas) is IslaiduIrasas:
                balansas -= irasas.suma
        return balansas

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)
