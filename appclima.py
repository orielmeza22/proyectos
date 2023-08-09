import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class AppClima(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App Meteorológica")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_titulo = QLabel("Consulta el Clima")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_titulo)

        self.entry_ciudad = QLineEdit()
        self.entry_ciudad.setPlaceholderText("Ingresa una ciudad")
        layout.addWidget(self.entry_ciudad)

        self.boton_consultar = QPushButton("Consultar")
        self.boton_consultar.clicked.connect(self.obtener_clima)
        layout.addWidget(self.boton_consultar)

        self.label_clima = QLabel("")
        self.label_clima.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_clima)

        self.label_icono = QLabel()
        self.label_icono.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_icono)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def obtener_clima(self):
        ciudad = self.entry_ciudad.text()

        if ciudad:
            API_KEY = "ccd6a27349186ff690fd04f07a35ddc0"
            API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"

            response = requests.get(API_URL)
            data = response.json()

            if response.status_code == 200:
                temperatura = data["main"]["temp"]
                descripcion = data["weather"][0]["description"]
                icono_id = data["weather"][0]["icon"]

                resultado = f"Temperatura: {temperatura} °C\n{descripcion.capitalize()}"
                self.label_clima.setText(resultado)

                icono_url = f"http://openweathermap.org/img/w/{icono_id}.png"
                pixmap = QPixmap(icono_url)
                self.label_icono.setPixmap(pixmap)
            else:
                self.label_clima.setText("Error al obtener datos del clima")
                self.label_icono.clear()
        else:
            self.label_clima.setText("Ingresa una ciudad válida")
            self.label_icono.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AppClima()
    ventana.show()
    sys.exit(app.exec_())
