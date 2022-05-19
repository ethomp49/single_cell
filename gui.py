from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QTabBar
from import_page import *
from histogram_page import *
from consecutive_page import *
from particle_page import *
from collected_page import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Single Cell Data Processor")
        self.setMinimumSize(1005, 600)

        self.main_window = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_window.setLayout(self.main_layout)
        self.setCentralWidget(self.main_window)

        self.tab_bar = QTabBar()
        tabs = ["Current Data", "Histogram", "Consecutive Particles", "Corrected Particle Data", "Collected Data"]
        for tab in tabs:
            self.tab_bar.addTab(tab)
        self.main_layout.addWidget(self.tab_bar)

        self.stack = QStackedWidget()

        # -------------------------------------------- Import Page --------------------------------------------

        self.import_tab = ImportPage()

        # ----------------------------------------Histogram Window-----------------------------------------------------

        self.histogram_tab = HistogramPage()

        # ----------------------------------Consecutive Particles Window-----------------------------------------------

        self.consecutive_particles_window = QWidget()

        # --------------------------------------Particle Data Window---------------------------------------------------

        self.corrected_particle_data_window = QWidget()

        self.collected_data_window = QWidget()

        stack_widgets = [self.import_tab, self.histogram_tab, self.consecutive_particles_window,
                         self.corrected_particle_data_window, self.collected_data_window]
        for widget in stack_widgets:
            self.stack.addWidget(widget)

        self.main_layout.addWidget(self.stack)

        self.tab_bar.tabBarClicked.connect(self.tab_bar_clicked)

        self.show()

    def tab_bar_clicked(self, index):
        self.stack.setCurrentIndex(index)
