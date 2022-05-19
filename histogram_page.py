from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCharts import QChart, QChartView, QValueAxis
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt


class HistogramPage(QWidget):
    def __init__(self):
        super(HistogramPage, self).__init__()

        self.page_layout = QVBoxLayout()
        self.setLayout(self.page_layout)

        sections = [ChartSection(), InputSection()]
        self.chart_section, self.input_section = sections

        for section in sections:
            self.page_layout.addWidget(section)


class ChartSection(QChartView):
    def __init__(self):
        super(ChartSection, self).__init__()

        self.chart = QChart()
        self.chart.setTitle('Signal Distribution')

        self.x_axis, self.y_axis = [QValueAxis(), QValueAxis()]

        self.x_axis.setRange(0, 1)
        self.x_axis.setTitleText('Signal (counts)')
        self.chart.addAxis(self.x_axis, Qt.AlignmentFlag.AlignBottom)

        self.y_axis.setRange(0, 1)
        self.y_axis.setTitleText('Frequency')
        self.chart.addAxis(self.y_axis, Qt.AlignmentFlag.AlignLeft)

        self.setChart(self.chart)


class InputSection(QWidget):
    def __init__(self):
        super(InputSection, self).__init__()

        self.section_layout = QHBoxLayout()
        self.setLayout(self.section_layout)

        widgets = [QLabel('Bin Size'), QLineEdit(), QPushButton('Plot Distribution')]
        self.label, self.field, self.button = widgets

        self.label.setFixedWidth(600)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.validator = QIntValidator()
        self.field.setValidator(self.validator)
        self.field.setFixedWidth(100)

        for widget in widgets:
            self.section_layout.addWidget(widget)
