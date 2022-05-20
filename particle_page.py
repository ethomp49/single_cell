from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QHeaderView, QPushButton
from PyQt6.QtCharts import QChart, QChartView, QBarSeries, QValueAxis
from PyQt6.QtCore import Qt
from histogram_page import HistogramPage
from consecutive_page import TableSection


class ParticlePage(QWidget):
    def __init__(self):
        super(ParticlePage, self).__init__()

        self.page_layout = QHBoxLayout()
        self.setLayout(self.page_layout)

        sections = [TableExportSection(), HistogramPage('Corrected Particle Distribution')]
        self.table_section, self.chart_section = sections

        self.table_section.setFixedWidth(500)

        for section in sections:
            self.page_layout.addWidget(section)


class TableExportSection(QWidget):
    def __init__(self):
        super(TableExportSection, self).__init__()

        self.section_layout = QVBoxLayout()
        self.setLayout(self.section_layout)

        self.table = TableSection()

        self.export_button = QPushButton('Export Data')

        for widget in [self.table, self.export_button]:
            self.section_layout.addWidget(widget)
#
#
# class ChartSection(QWidget):
#    def __init__(self):
#        super(ChartSection, self).__init__()
#
#        self.section_layout = QVBoxLayout()
#        self.setLayout(self.section_layout)
#
#        self.chart = QChart()
#        self.chart.setTitle('Corrected Particle Distribution')
#        self.chart_view = QChartView()
#
#        self.x_axis = QValueAxis()
#        self.x_axis.setRange(0, 1)
#        self.x_axis.setTitleText('Signal (counts)')
#        self.chart.addAxis(self.x_axis, Qt.AlignmentFlag.AlignBottom)
#
#        self.y_axis = QValueAxis()
#        self.y_axis.setRange(0, 1)
#        self.y_axis.setTitleText('Frequency')
#        self.chart.addAxis(self.y_axis, Qt.AlignmentFlag.AlignLeft)
#
#        self.chart_view.setChart(self.chart) #
