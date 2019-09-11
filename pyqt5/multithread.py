from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget
from typing import *

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)

class Worker(QRunnable):
    def __init__(self,fn,*args,**kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            result =

class MainWindow(QMainWindow):
    counter: int

    def __init__(self):
        super().__init__()
        self.counter = 0

        layout = QVBoxLayout()
        self.l = QLabel('Start')
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        c = QPushButton("?")
        c.pressed.connect(self.change_message)

        layout.addWidget(self.l)
        layout.addWidget(b)
        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)
        self.show()

    def change_message(self):
        self.message = "OH NO"

    def oh_no(self):
