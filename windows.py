import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow ):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bottom-Right Window')
        self.resize(400, 300)  # Set the initial size of the window

        # Get the screen size and the window size
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        window_size = self.size()

        # Calculate the bottom-right position
        bottom_right_x = screen_size.width() - window_size.width()
        bottom_right_y = screen_size.height() - window_size.height()

        # Move the window to the bottom-right corner
        self.move(bottom_right_x, bottom_right_y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
