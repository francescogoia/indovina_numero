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
                                     disabled=True, value=self._controller.getNmax())
        self._txtMmax = ft.TextField(label="Tentativi Max", width=100,
                                     disabled=True, value=self._controller.getMmax())
        self._txtMrim = ft.TextField(label="Tentativi Rim", width=100,
                                     disabled=True, value=self._controller.getMrim())

        row1 = ft.Row([self._txtNmax, self._txtMmax, self._txtMrim],
                      alignment=ft.MainAxisAlignment.CENTER)
        ## Row2
        self._txtTentativo = ft.TextField(label="Tentativo", disabled=True)
        self._btnNuova = ft.ElevatedButton(text="Nuova partita",
                                           on_click = self._controller.handleNuova)
        self._btnProva = ft.ElevatedButton(text="Prova",
                                           on_click = self._controller.handleProva,
                                           disabled=True)

        row2 = ft.Row([self._btnNuova, self._txtTentativo, self._btnProva],
                      alignment=ft.MainAxisAlignment.CENTER)

        ## Row3
        self._lvOut = ft.ListView()



        self._page.add(self._titolo, row1, row2, self._lvOut)

    def setController(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()
