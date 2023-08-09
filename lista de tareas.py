import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem

class ListaTareasApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista de Tareas - Tema Oscuro")
        self.setGeometry(100, 100, 400, 500)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label_titulo = QLabel("Lista de Tareas")
        label_titulo.setStyleSheet("color: #FFFFFF; font-size: 18pt; font-weight: bold;")
        layout.addWidget(label_titulo)

        self.entry_tarea = QLineEdit()
        self.entry_tarea.setStyleSheet("background-color: #313131; color: #FFFFFF;")
        layout.addWidget(self.entry_tarea)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: #2ECC71; color: #FFFFFF;")
        boton_agregar.clicked.connect(self.agregar_tarea)
        layout.addWidget(boton_agregar)

        self.lista = QListWidget()
        self.lista.setStyleSheet("background-color: #2C3E50; color: #FFFFFF;")
        layout.addWidget(self.lista)

        boton_marcar = QPushButton("Marcar Completada")
        boton_marcar.setStyleSheet("background-color: #E74C3C; color: #FFFFFF;")
        boton_marcar.clicked.connect(self.marcar_completada)
        layout.addWidget(boton_marcar)

        boton_eliminar = QPushButton("Eliminar Tarea")
        boton_eliminar.setStyleSheet("background-color: #E74C3C; color: #FFFFFF;")
        boton_eliminar.clicked.connect(self.eliminar_tarea)
        layout.addWidget(boton_eliminar)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def agregar_tarea(self):
        tarea = self.entry_tarea.text()
        if tarea:
            self.lista.addItem(QListWidgetItem(tarea))
            self.entry_tarea.clear()

    def marcar_completada(self):
        tarea_item = self.lista.currentItem()
        if tarea_item:
            tarea_texto = tarea_item.text()
            tarea_item.setText("✓ " + tarea_texto)

    def eliminar_tarea(self):
        tarea_item = self.lista.currentItem()
        if tarea_item:
            self.lista.takeItem(self.lista.row(tarea_item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ListaTareasApp()
    ventana.show()
    sys.exit(app.exec_())
