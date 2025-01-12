from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QCheckBox, QWidget, QHBoxLayout, QPushButton, QHeaderView
)


class LocationApp(QWidget):
    def __init__(self, locations):
        super().__init__()
        self.setWindowTitle("Location List")
        self.setGeometry(200, 200, 600, 400)

        # Main layout
        main_layout = QVBoxLayout()

        # Check all checkbox
        self.check_all_checkbox = QCheckBox("Check All")
        self.check_all_checkbox.stateChanged.connect(self.toggle_check_all)

        # Save and Close buttons
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_action)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        # Layout for buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.close_button)

        # Table widget
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(len(locations))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Select", "Name", "Latitude", "Longitude"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Populate the table
        self.populate_table(locations)

        # Add all widgets to main layout
        main_layout.addWidget(self.check_all_checkbox)
        main_layout.addWidget(self.table_widget)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def populate_table(self, locations):
        """Populate the table with locations."""
        for row, (name, lat, lon) in enumerate(locations):
            # Create checkbox for each row
            checkbox = QCheckBox()
            self.table_widget.setCellWidget(row, 0, checkbox)

            # Create table cells for Name, Latitude, and Longitude
            self.table_widget.setItem(row, 1, QTableWidgetItem(name))
            self.table_widget.setItem(row, 2, QTableWidgetItem(lat))
            self.table_widget.setItem(row, 3, QTableWidgetItem(lon))

    def toggle_check_all(self):
        """Toggle the state of all checkboxes based on 'Check All' checkbox."""
        state = self.check_all_checkbox.isChecked()
        for row in range(self.table_widget.rowCount()):
            checkbox = self.table_widget.cellWidget(row, 0)
            checkbox.setChecked(state)

    def save_action(self):
        """Save action: can be customized to save checked locations."""
        checked_locations = []
        for row in range(self.table_widget.rowCount()):
            checkbox = self.table_widget.cellWidget(row, 0)
            if checkbox.isChecked():
                name = self.table_widget.item(row, 1).text()
                lat = self.table_widget.item(row, 2).text()
                lon = self.table_widget.item(row, 3).text()
                checked_locations.append((name, lat, lon))
        print("Checked Locations:", checked_locations)
        # Here, you can save the checked_locations to a file or database.

    def close(self):
        """Close the application."""
        QApplication.quit()


if __name__ == "__main__":
    import sys

    # Sample data: List of locations
    locations = [
        ("Location A", "12.9716", "77.5946"),
        ("Location B", "28.7041", "77.1025"),
        ("Location C", "19.0760", "72.8777"),
        ("Location D", "13.0827", "80.2707"),
        ("Location E", "22.5726", "88.3639"),
    ]

    app = QApplication(sys.argv)
    window = LocationApp(locations)
    window.show()
    sys.exit(app.exec_())
