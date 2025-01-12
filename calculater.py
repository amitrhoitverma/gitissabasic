import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        try:
            super(MainWindow,self).__init__()
            uic.loadUi("calculter.ui",self)
            self.setWindowTitle("Calculater")

            screen = QApplication.primaryScreen()
            screen_size = screen.size()
            window_size = self.size()

            # Calculate the bottom-right position
            bottom_right_x = screen_size.width() - window_size.width()
            bottom_right_y = screen_size.height() - window_size.height()

            # Move the window to the bottom-right corner
            self.move(bottom_right_x, bottom_right_y)

            self.ADD.clicked.connect(self.add)
            self.SUB.clicked.connect(self.sub)
            self.MUL.clicked.connect(self.mul)
            self.DIV.clicked.connect(self.div)
            self.DIV_2.clicked.connect(self.mod)
            self.DIV_3.clicked.connect(self.exp)
            self.DIV_4.clicked.connect(self.flo)
        except:
            print("An exception occurred in MainWindow")
    def Cal(self):
        try:
           FirstN = int(self.F.text())
           SecondN = int(self.S.text())
           return FirstN,SecondN
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception in Cal@Calculater",exc_type, fname, exc_tb.tb_lineno)

    def add(self):
        try:
            First_number, Second_number = self.Cal()
            sum = First_number + Second_number
            print(sum)
            self.F_2.setText(str(sum))
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception in add @Calculater", exc_type, fname, exc_tb.tb_lineno)
    def sub(self):
        try:
            First_number, Second_number = self.Cal()
            sub = First_number - Second_number
            print(sub)
            self.F_2.setText(str(sub))
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception in sub @Calculater", exc_type, fname, exc_tb.tb_lineno)
    def mul(self):
        try:
            First_number, Second_number = self.Cal()
            mul = First_number * Second_number
            print(mul)
            self.F_2.setText(str(mul))
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception in mul @Calculater", exc_type, fname, exc_tb.tb_lineno)
    def div(self):
        try:
            First_number, Second_number = self.Cal()
            div = First_number / Second_number
            print(div)
            self.F_2.setText(str(div))
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception in div @Calculater", exc_type, fname, exc_tb.tb_lineno)
    def mod(self):
        try:
            First_number, Second_number = self.Cal()
            div = First_number % Second_number
            print(div)
            self.F_2.setText(str(div))
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception in div @Calculater", exc_type, fname, exc_tb.tb_lineno)
    def exp(self):
        try:
            First_number, Second_number = self.Cal()
            div = First_number ** Second_number
            print(div)
            self.F_2.setText(str(div))
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception in exp @Calculater", exc_type, fname, exc_tb.tb_lineno)
    def flo(self):
        try:
            First_number, Second_number = self.Cal()
            div = First_number // Second_number
            print(div)
            self.F_2.setText(str(div))
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Exception in flo @Calculater", exc_type, fname, exc_tb.tb_lineno)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
