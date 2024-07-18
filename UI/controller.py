import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.country = None
        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        for country in self._model.countries:
            self._view.ddcountry.options.append(ft.dropdown.Option(key = country,
                                                                   data = country,
                                                                   on_click= self.read_ddcountry))

        for i in range(2015,2019):
            self._view.ddyear.options.append(ft.dropdown.Option(str(i)))

    def read_ddcountry(self, e):
        print("read_DD_country called ")
        if e.control.data is None:
            self.country = None
        else:
            self.country = e.control.data

    def handle_graph(self, e):
        self._model.buildGraph(self.country, self._view.ddyear.value)
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {len(self._model.myGraph.nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {len(self._model.myGraph.edges)}"))
        self._view.update_page()



    def handle_volume(self, e):
        dict = self._model.volumi()
        lista_prodotti = list(dict.items())
        lista_prodotti.sort(key = lambda x : x[1])
        lista_prodotti.reverse()
        for element in lista_prodotti:
            if element[1] != 0:
                name = self._model.dict[int(element[0])]
                self._view.txtOut2.controls.append(ft.Text(f"{name} --> {element[1]}"))
        self._view.update_page()




    def handle_path(self, e):
        if int(self._view.txtN.value) >= 2:
            for node in self._model.myGraph.nodes:
                partial = []
                partial.append(node)
                self._model.ricorsione(partial, int(self._view.txtN.value))
            print(f"somma pari a {self._model.somma}")
        else:
            self._view.create_alert("Inserire una lunghezza minima pari a 2")

