from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit,
    QPushButton, QListWidget, QMessageBox
)


class LatLonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Latitude and Longitude Input")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()

        # Input fields layout
        input_layout = QHBoxLayout()
        self.lat_input = QLineEdit(self)
        self.lat_input.setPlaceholderText("Enter Latitude")
        self.lon_input = QLineEdit(self)
        self.lon_input.setPlaceholderText("Enter Longitude")
        input_layout.addWidget(QLabel("Latitude:"))
        input_layout.addWidget(self.lat_input)
        input_layout.addWidget(QLabel("Longitude:"))
        input_layout.addWidget(self.lon_input)

        # Buttons layout
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_lat_lon)
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_list)
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.clear_button)

        # List widget to display entries
        self.list_widget = QListWidget()

        # Add components to the main layout
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def add_lat_lon(self):
        lat = self.lat_input.text().strip()
        lon = self.lon_input.text().strip()

        if not self.validate_input(lat, lon):
            QMessageBox.warning(self, "Input Error", "Please enter valid latitude and longitude values.")
            return

        self.list_widget.addItem(f"Latitude: {lat}, Longitude: {lon}")
        self.lat_input.clear()
        self.lon_input.clear()

    def validate_input(self, lat, lon):
        try:
            lat = float(lat)
            lon = float(lon)
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                return True
        except ValueError:
            pass
        return False

    def clear_list(self):
        self.list_widget.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = LatLonApp()
    window.show()
    sys.exit(app.exec_())
