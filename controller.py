from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()


    def handleNuova(self, e):
        self._view._txtMrim.value = self.getMmax()
        self._view._btnProva.disabled = False
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Indovina il numero", color="green"))
        self._view._txtTentativo.disabled = False
        self._model.inizializza()
        self._view.update()


    def handleProva(self, e):
        tentativo = self._view._txtTentativo.value
        self._view._txtTentativo.value = ""
        try:
            int_tentativo = int(tentativo)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Il tentativo deve essere un intero", color="red"))
            self._view.update()
            return

        mRim, risultato = self._model.indovina(int_tentativo)

        self._view._txtMrim.value = mRim
        self._view.update()

        if mRim == 0:
            self._view._btnProva.disabled = True
            self._view._txtTentativo.disabled = True
            self._view._lvOut.controls.append(ft.Text("Hai perso, il segreto era: " + str(self._model.segreto)))
            self._view.update()
            return

        if risultato == 0:
            self._view._lvOut.controls.append(ft.Text("Hai vinto"))
            self._view._btnProva.disabled = True
            self._view.update()
            return
        elif risultato == -1:
            self._view._lvOut.controls.append(ft.Text("No, il segreto è più piccolo"))
            self._view.update()
            return
        elif risultato == 1:
            self._view._lvOut.controls.append(ft.Text("No, il segreto è più grande"))
            self._view.update()
            return

    def getNmax(self):
        return self._model.NMax

    def getMmax(self):
        return self._model.Mmax

    def getMrim(self):
        return self._model.Mrim
