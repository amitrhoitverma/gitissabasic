import sys
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout, \
    QPushButton
from qtpy.QtGui import QImage, QPixmap
from qtpy.QtCore import Qt


class ImageToTableApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        self.layout = QVBoxLayout()

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        # Create a table to display pixel data
        self.table = QTableWidget(self)
        self.layout.addWidget(self.table)

        # Button to load image and populate the table
        self.load_button = QPushButton("Load Image", self)
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        # Set the layout of the window
        self.setLayout(self.layout)
        self.setWindowTitle("Image to Table")
        self.resize(800, 600)

    def load_image(self):
        # Load image using QImage (can be any image path)
        image_path = "path_to_your_image.jpg"  # Replace with your image path
        image = QImage(image_path)

        # Display image on QLabel
        self.image_label.setPixmap(QPixmap.fromImage(image).scaled(400, 400, Qt.KeepAspectRatio))

        # Convert the image into pixel data
        self.populate_table(image)

    def populate_table(self, image):
        # Get image size
        width = image.width()
        height = image.height()

        # Set the table row and column count
        self.table.setRowCount(height)
        self.table.setColumnCount(width)

        # Populate the table with pixel values (R, G, B)
        for row in range(height):
            for col in range(width):
                # Get pixel color
                color = image.pixelColor(col, row)
                # Get RGB values
                r, g, b = color.red(), color.green(), color.blue()
                # Insert RGB value into the table
                self.table.setItem(row, col, QTableWidgetItem(f"{r},{g},{b}"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageToTableApp()
    window.show()
    sys.exit(app.exec_())
