from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
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
        self.clear_button = QPushButton("Clear All")
        self.clear_button.clicked.connect(self.clear_table)
        self.clear_last_button = QPushButton("Clear Last")
        self.clear_last_button.clicked.connect(self.clear_last_item)
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.clear_last_button)
        button_layout.addWidget(self.clear_button)

        # Table widget to display entries
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)  # Two columns: Latitude, Longitude
        self.table_widget.setHorizontalHeaderLabels(["Latitude", "Longitude"])

        # Remove row headers
        self.table_widget.verticalHeader().setVisible(False)

        # Add components to the main layout
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

    def add_lat_lon(self):
        lat = self.lat_input.text().strip()
        lon = self.lon_input.text().strip()

        if not self.validate_input(lat, lon):
            QMessageBox.warning(self, "Input Error", "Please enter valid latitude and longitude values.")
            return

        # Format latitude and longitude to 4 decimal places
        lat = f"{float(lat):.4f}"
        lon = f"{float(lon):.4f}"

        # Add a new row to the table
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)

        # Add the formatted latitude and longitude values to the respective columns
        lat_item = QTableWidgetItem(lat)
        lon_item = QTableWidgetItem(lon)

        # Center-align the items
        lat_item.setTextAlignment(Qt.AlignCenter)
        lon_item.setTextAlignment(Qt.AlignCenter)

        self.table_widget.setItem(row_position, 0, lat_item)
        self.table_widget.setItem(row_position, 1, lon_item)

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

    def clear_table(self):
        self.table_widget.setRowCount(0)

    def clear_last_item(self):
        row_count = self.table_widget.rowCount()
        if row_count > 0:
            self.table_widget.removeRow(row_count - 1)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = LatLonApp()
    window.show()
    sys.exit(app.exec_())
