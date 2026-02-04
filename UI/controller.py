import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        role = self._view.dd_ruolo.value
        self._model.build_graph(role)

        self._view.list_risultato.controls.clear()

        self._view.list_risultato.controls.append(
            ft.Text(f"Numero di nodi: {self._model.get_num_of_nodes()} "
                    f"Numero di archi: {self._model.get_num_of_edges()}"))

        self._view.btn_classifica.disabled = False
        self._view.update()
    def handle_classifica(self):
        classifica = self._model.classifica()
        self._view.list_risultato.controls.append(ft.Text(f"artisti in ordine decrescente di influenza:"))
        for a in classifica:
            self._view.list_risultato.controls.append(ft.Text(f"{a[0].name} delta = {a[1]}"))
        self._view.update()

    def handle_dd_roles(self,e):
        role = self._view.dd_ruolo.value

    def populate_dd_roles(self):
        for role in self._model.roles:
            self._view.dd_ruolo.options.append(ft.dropdown.Option(role))

        self._view.update()