# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:31:06 2024

@author: SIB7BU
"""

# main.py
import sys
from PyQt5.QtWidgets import QApplication
from utils.pencere_modulu import Pencere



def main():
    app = QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
    


