import os
import sys
import time
import threading

import numpy as np
import PIL.ImageGrab
import cv2
import win32api
import win32con
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

from ui_controller.view import main_window
from ui_controller.button_event import btn_events
from ui_controller.canvas_handler import canvasHandler
from utils.utils import playMGS

class main():
    def __init__(self):
        self.button_events = btn_events(self)
        self.win = main_window(self.button_events)
        self.win.show()
        self.canvasHandler = canvasHandler(self.win, self.win.ui.label)
        self.canvasHandler.frameSignal.connect(self.win.display_video)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec_())