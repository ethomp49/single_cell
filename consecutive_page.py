from PyQt6.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QHeaderView, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt


class ConsecutivePage(QWidget):
    def __init__(self):
        super(ConsecutivePage, self).__init__()

        self.page_layout = QVBoxLayout()
        self.setLayout(self.page_layout)

        sections = [TableSection(), CounterSection()]
        self.table_section, self.counter_section = sections

        for section in sections:
            self.page_layout.addWidget(section)


class TableSection(QTableWidget):
    def __init__(self):
        super(TableSection, self).__init__()

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['Particle Index', 'Particle Time (s)', 'Particle Signal (counts)'])
        self.horizontalHeader().setSectionsClickable(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.verticalHeader().setVisible(False)


class CounterSection(QWidget):
    def __init__(self):
        super(CounterSection, self).__init__()

        self.section_layout = QHBoxLayout()
        self.setLayout(self.section_layout)

        self.particles = QLabel('Consecutive Particles Detected: 0')
        self.clusters = QLabel('Consecutive Particle Clusters: 0')

        for widget in [self.particles, self.clusters]:
            widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.section_layout.addWidget(widget)
