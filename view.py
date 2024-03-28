import flet as ft


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)
        ## Row1
        self._txtNmax = ft.TextField(label="N Max", width=100,
                                     disabled=True, value=self._controller.getNmax(), visible= False)
        self._txtMmax = ft.TextField(label="Tentativi Max", width=100,
                                     disabled=True, value=self._controller.getMmax(), visible= False)
        self._txtMrim = ft.TextField(label="Tentativi Rim", width=100,
                                     disabled=True, value=self._controller.getMrim(), visible= False)

        row1 = ft.Row([self._txtNmax, self._txtMmax, self._txtMrim],
                      alignment=ft.MainAxisAlignment.CENTER)
        ## Row2
        self._txtTentativo = ft.TextField(label="Tentativo", disabled=True)
        self._btnNuova = ft.ElevatedButton(text="Nuova partita",
                                           on_click = self._controller.handleNuova, disabled=True)
        self._btnProva = ft.ElevatedButton(text="Prova",
                                           on_click = self._controller.handleProva,
                                           disabled=True)
        self._btnAbbandona = ft.ElevatedButton(text="Abbandona",
                                               on_click = self._controller.handleAbbandona,
                                               disabled=True)
        row2 = ft.Row([self._btnNuova, self._txtTentativo, self._btnProva, self._btnAbbandona],
                      alignment=ft.MainAxisAlignment.CENTER)
        ## Row3

        self._txtConfermaDifficolta = ft.Text("Scegliere la difficoltà")
        self._selettoreDifficolta = ft.Dropdown(label="Selezionare la difficoltà",
                                                on_change=self._confermaSelezionatoDifficolta)
        self._fillSelettoreDifficolta()
        row3 = ft.Row([self._txtConfermaDifficolta, self._selettoreDifficolta])
        ## Row4
        self._progBar = ft.ProgressBar(width=300, color="green", visible=False)
        self._txtVita = ft.Text("Vite rimanenti", visible=False)
        row4 = ft.Row([self._txtVita, self._progBar])
        ## Row5
        self._intervallo = ft.Text(f"Intervallo: ", visible=False)
        row5 = ft.Row([self._intervallo])
        ## Row6
        self._lvOut = ft.ListView()

        self._page.add(self._titolo, row1, row2, row3, row4, row5, self._lvOut)

    def setController(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()

    def _fillSelettoreDifficolta(self):
        for i in ["Facile", "Media", "Difficile"]:
            self._selettoreDifficolta.options.append(ft.dropdown.Option(i))

    def _confermaSelezionatoDifficolta(self, e):
        if self._selettoreDifficolta.value == "":
            self._txtConfermaDifficolta.value = "Selezionare la difficoltà"
            self.update()
        else:
            self._txtConfermaDifficolta.value = f"Difficoltà {self._selettoreDifficolta.value} selezionata"
            self._controller.esponiParametri()
            self._esponiParametri()
            self.update()

    def _esponiParametri(self):
        self._txtNmax.visible = True
        self._txtMrim.visible = True
        self._txtMmax.visible = True
        self.update()