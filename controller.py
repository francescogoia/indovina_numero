from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()
        self._inferiore = 0
        self._superiore = self._model.NMax
        self._intervallo = [self._inferiore, self._superiore]
        self._numeriInseriti = []


    def handleAbbandona(self, e):
        self._view._lvOut.controls.append(ft.Text("Hai abbandonato la partita", color="blue"))
        self._view._btnProva.disabled = True
        self._view._txtTentativo.disabled = True
        self._view._btnNuova.disabled = False
        self._view.update()


    def esponiParametri(self):
        if self._view._selettoreDifficolta.value == "Facile":
            self._view._btnNuova.disabled = False
            self._model.difficoltaFacile()
        elif self._view._selettoreDifficolta.value == "Media":
            self._view._btnNuova.disabled = False
            self._model.difficoltaMedia()
        elif self._view._selettoreDifficolta.value == "Difficile":
            self._view._btnNuova.disabled = False
            self._model.difficoltaDifficile()

        self._view._txtNmax.value = self.getNmax()
        self._view._txtMmax.value = self.getMmax()
        self._view._txtMrim.value = self.getMrim()


    def handleNuova(self, e):
    ##    self._view._txtMrim.value = self.getMmax()
        self._view._btnProva.disabled = False
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Indovina il numero", color="green"))
        self._view._txtTentativo.disabled = False
        self._view._btnAbbandona.disabled = False
        self._view._progBar.visible = True
        self._view._progBar.value = 1
        self._view._txtVita.visible = True

        self._model.inizializza()
        self._view.update()


    def handleProva(self, e):
        self._view._btnNuova.disabled = True
        tentativo = self._view._txtTentativo.value
        self._view._txtTentativo.value = ""
        try:
            int_tentativo = int(tentativo)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Il tentativo deve essere un intero", color="red"))
            self._view.update()
            return

        self._numeriInseriti.append(int_tentativo)


        mRim, risultato = self._model.indovina(int_tentativo)

        self._view._txtMrim.value = mRim

        self._view.update()

        if mRim == 0:
            self._view._btnProva.disabled = True
            self._view._txtTentativo.disabled = True
            self._view._lvOut.controls.append(ft.Text("Hai perso, il segreto era: " + str(self._model.segreto)))
            self._view._btnAbbandona.disabled = True
            self._view._progBar.value = 0
            self._view.update()
            return

        if risultato == 0:
            self._view._lvOut.controls.append(ft.Text("Hai vinto"))
            self._view._btnProva.disabled = True
            self._view._btnNuova.disabled = False
            self._view.update()
            return
        elif risultato == -1:
            self._view._lvOut.controls.append(ft.Text("No, il segreto è più piccolo"))
            self._view._progBar.value = mRim / self._model.Mmax
            self._intervallo[1] = int_tentativo - 1
            self._view._intervallo.value = f"Intervallo: {self._intervallo}"
            self._view._intervallo.visible = True
            if self._controlloGiaInserito() == True:
                self._view._lvOut.controls.append(ft.Text(f"Il numero {tentativo} è già stato inserito"))
            self._view.update()
            return
        elif risultato == 1:
            self._view._lvOut.controls.append(ft.Text("No, il segreto è più grande"))
            self._view._progBar.value = mRim / self._model.Mmax
            self._intervallo[0] = int_tentativo + 1
            self._view._intervallo.value = f"Intervallo: {self._intervallo}"
            self._view._intervallo.visible = True
            if self._controlloGiaInserito() == True:
                self._view._lvOut.controls.append(ft.Text(f"Il numero {tentativo} è già stato inserito"))
            self._view.update()
            return


    def getNmax(self):
        return self._model.NMax

    def getMmax(self):
        return self._model.Mmax

    def getMrim(self):
        return self._model.Mrim

    def _controlloGiaInserito(self):
        if len(self._numeriInseriti) != len(set(self._numeriInseriti)):
            self._numeriInseriti = list(set(self._numeriInseriti))          ## dopo che mi accerto che la lunghezza era diversa resetto la lunghezza,
            return True                                                     ## altrimenti anche se inserisco un nuovo numero la funzione returna True
