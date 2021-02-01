from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

from utils.utils import normalize_points
from ui.main_ui import main_form

class main_window(QMainWindow):
    def __init__(self, event):
        QMainWindow.__init__(self)
        self.ui = main_form(self, event)
        self.setWindowTitle('串流畫框')
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def get_draw_point(self):
        return [p for p in self.points]

    def display_video(self, args ,color = (0,255,0)):
        frame, size, label = args
        draw_points = [p for p in self.points]
        if len(draw_points) == 1:
            cv2.circle(frame, draw_points[0], 1, (0,255,0), 4)
        elif len(draw_points) > 1:
            for i in range(1 ,len(draw_points)):
                cv2.line(frame, draw_points[i-1], draw_points[i], (0,255,0),2)
        width, height = size
        bytesPerComponent = 3
        bytesPerLine = bytesPerComponent * width
        qimg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        qimg = QPixmap.fromImage(qimg)
        label.setPixmap(qimg)