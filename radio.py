from qtpy.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QRadioButton, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Button Frames")
        self.setGeometry(100, 100, 400, 300)

        # Create Frames
        self.create_color_frame()
        self.create_mode_frame()
        self.create_type_frame()

        # Label to show the operation result
        self.result_label = QLabel("Select options to see the operation.", self)
        self.result_label.setGeometry(20, 250, 360, 30)

        # Confirm button
        self.confirm_button = QPushButton("Confirm Selection", self)
        self.confirm_button.setGeometry(150, 220, 120, 30)
        self.confirm_button.clicked.connect(self.execute_operation)

    def create_color_frame(self):
        self.color_frame = QFrame(self)
        self.color_frame.setGeometry(20, 20, 120, 100)
        self.color_frame.setFrameShape(QFrame.Box)

        layout = QVBoxLayout(self.color_frame)
        self.red_rb = QRadioButton("Red")
        self.blue_rb = QRadioButton("Blue")
        self.yellow_rb = QRadioButton("Yellow")
        layout.addWidget(self.red_rb)
        layout.addWidget(self.blue_rb)
        layout.addWidget(self.yellow_rb)

    def create_mode_frame(self):
        self.mode_frame = QFrame(self)
        self.mode_frame.setGeometry(150, 20, 120, 100)
        self.mode_frame.setFrameShape(QFrame.Box)

        layout = QVBoxLayout(self.mode_frame)
        self.scenario_rb = QRadioButton("Scenario")
        self.actual_rb = QRadioButton("Actual")
        layout.addWidget(self.scenario_rb)
        layout.addWidget(self.actual_rb)

    def create_type_frame(self):
        self.type_frame = QFrame(self)
        self.type_frame.setGeometry(280, 20, 120, 100)
        self.type_frame.setFrameShape(QFrame.Box)

        layout = QVBoxLayout(self.type_frame)
        self.air_rb = QRadioButton("Air")
        self.navy_rb = QRadioButton("Navy")
        layout.addWidget(self.air_rb)
        layout.addWidget(self.navy_rb)

    #
    def execute_operation(self):
        # Get the selected options
        color = "Red" if self.red_rb.isChecked() else \
            "Blue" if self.blue_rb.isChecked() else \
                "Yellow" if self.yellow_rb.isChecked() else None

        mode = "Scenario" if self.scenario_rb.isChecked() else \
            "Actual" if self.actual_rb.isChecked() else None

        type_ = "Air" if self.air_rb.isChecked() else \
            "Navy" if self.navy_rb.isChecked() else None

        # Perform the operation based on the selected combination
        if color and mode and type_:
            self.result_label.setText(f"Operation: {color} + {mode} + {type_}")
        else:
            self.result_label.setText("No valid selection made.")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
