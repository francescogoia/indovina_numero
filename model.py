import random


class Model(object):
    def __init__(self):
        self._NMax = 100             ## fondo scala
        self._Mmax = 6               ## numero max tentativi
        self._Mrim = self._Mmax
        self._segreto = None

    @property
    def NMax(self):
        return self._NMax
    @property
    def Mmax(self):
        return self._Mmax
    @property
    def Mrim(self):
        return self._Mrim
    @property
    def segreto(self):
        return self._segreto


    def inizializza(self):
        self._segreto = random.randint(1, self._NMax)
        self._Mrim = self._Mmax         ## ridiamo le vite al giocatore
        print(self._segreto)

    def indovina(self, tentativo):
        if self._Mrim == 0 :
            return self._Mrim, None         ## restituisco le vite rimaste e il risultato del tentativo
        else:
            self._Mrim = self._Mrim - 1

        if tentativo == self._segreto:
            return self._Mrim, 0
        elif tentativo > self._segreto:
            return self._Mrim, -1           ## devo ridurre il tentativo
        elif tentativo < self._segreto:
            return self._Mrim, 1            ## devo aumentare il tentativo
