from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QGridLayout, QTableWidgetItem, \
    QTableWidget, QLineEdit, QHeaderView
from PyQt6.QtCharts import QValueAxis, QChart, QChartView, QLineSeries
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QIntValidator


class ImportPage(QWidget):
    def __init__(self):
        super(ImportPage, self).__init__()
        self.page_layout = QVBoxLayout()

        # ---- Chart Section ----

        self.chart_section = ChartSection()
        self.page_layout.addWidget(self.chart_section)

        # ---- Import Section ----

        self.import_section = ImportSection()
        self.page_layout.addWidget(self.import_section)

        # ---- Parameters Section ----

        self.parameters_section = ParametersSection()
        self.page_layout.addWidget(self.parameters_section)

        # ---- Sample Info Section ----

        self.sample_info_section = SampleInfoSection()
        self.page_layout.addWidget(self.sample_info_section)

        # ---- Collection Section ----

        self.collection_section = CollectionSection()
        self.page_layout.addWidget(self.collection_section)

        self.setLayout(self.page_layout)


# ----Chart Section----

class ChartSection(QChartView):
    def __init__(self):
        super(ChartSection, self).__init__()

        self.x_axis = QValueAxis()
        self.x_axis.setTitleText("Time (s)")
        self.x_axis.setRange(0, 120)

        self.y_axis = QValueAxis()
        self.y_axis.setTitleText("Signal (counts)")
        self.y_axis.setRange(0, 1)

        self.data = QLineSeries()
        self.data_chart = QChart()
        self.data_chart.addAxis(self.x_axis, Qt.AlignmentFlag.AlignBottom)
        self.data_chart.addAxis(self.y_axis, Qt.AlignmentFlag.AlignLeft)

        self.setChart(self.data_chart)


# ----Import Section----

class ImportSection(QWidget):
    def __init__(self):
        super(ImportSection, self).__init__()

        # Setting a QHBoxLayout for the section

        self.import_layout = QHBoxLayout()
        self.setLayout(self.import_layout)

        # Creating the import button

        self.import_button = QPushButton("Import data")
        self.import_button.setFixedWidth(100)

        # Creating a label to display import status

        self.import_text = QLabel("No data selected")
        self.import_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Adding the widgets to the section

        for widget in [self.import_button, self.import_text]:
            self.import_layout.addWidget(widget)


# ----Parameters Section----

class ParametersSection(QWidget):
    def __init__(self):
        super(ParametersSection, self).__init__()

        # Validators

        self.int_validator = QIntValidator()
        self.double_validator = QDoubleValidator()

        # Setting a QGridLayout for the section

        self.parameters_layout = QGridLayout()
        self.setLayout(self.parameters_layout)

        # Creating the parameter fields

        self.stock_input = ParamField("Stock Concentration", self.double_validator, "particles/µL")
        self.dilution_input = ParamField("Dilution Factor", self.double_validator, "X")
        self.efficiency_input = ParamField("Transport Efficiency", self.double_validator, "%")
        self.sigma_input = ParamField("Sigma", self.int_validator, "")
        self.background_input = ParamField("Background Cutoff", self.int_validator, "counts")
        self.dwell_time_input = ParamField("Dwell Time", self.double_validator, "ms")

        # Adding parameters to the QGridLayout

        self.parameters_layout.addWidget(self.stock_input, 0, 0)
        self.parameters_layout.addWidget(self.dilution_input, 1, 0)
        self.parameters_layout.addWidget(self.efficiency_input, 2, 0)
        self.parameters_layout.addWidget(self.sigma_input, 0, 1)
        self.parameters_layout.addWidget(self.background_input, 1, 1)
        self.parameters_layout.addWidget(self.dwell_time_input, 2, 1)


# ----Sample Info Section----

class SampleInfoSection(QTableWidget):
    def __init__(self):
        super(SampleInfoSection, self).__init__()

        # Setting table size

        self.setRowCount(1)
        self.setColumnCount(8)
        self.setFixedHeight(55)

        # Setting column headers and removing row headers

        self.verticalHeader().setVisible(False)
        self.setHorizontalHeaderLabels(
            ['Particles Expected', 'Particles Counted', 'Max Signal(counts)', 'Min Signal(counts)',
             'Average Signal (counts)', 'Standard Deviation (counts)', 'Sigma', 'Background Cutoff (counts)'])

        # Setting column widths and turning resize and selection permissions off

        self.resizeColumnsToContents()
        self.horizontalHeader().setSectionsClickable(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        # Pre-populating the table with non-interactive items

        for col in range(0, self.columnCount()):
            blank_item = QTableWidgetItem()
            blank_item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.setItem(0, col, blank_item)


class CollectionSection(QWidget):
    def __init__(self):
        super(CollectionSection, self).__init__()

        # Setting a QHBoxLayout for the section

        self.collection_layout = QHBoxLayout()
        self.setLayout(self.collection_layout)

        # Creating label text

        self.sample_label_text = QLabel("Sample Label")
        self.sample_label_text.setFixedWidth(70)

        # Creating the label field

        self.sample_label_field = QLineEdit()

        # Creating the data collection button

        self.collect_button = QPushButton("Save Data To Table")
        self.collect_button.setFixedWidth(150)

        # Adding created widgets to the section

        for widget in [self.sample_label_text, self.sample_label_field, self.collect_button]:
            self.collection_layout.addWidget(widget)


# Custom class for parameters section

class ParamField(QWidget):
    def __init__(self, label, validator, unit):
        super(ParamField, self).__init__()

        self.label = QLabel(label)
        self.label.setFixedWidth(150)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.field = QLineEdit()
        self.field.setValidator(validator)

        self.unit = QLabel(unit)
        self.unit.setFixedWidth(100)

        self.field_layout = QHBoxLayout()
        self.field_layout.addWidget(self.label)
        self.field_layout.addWidget(self.field)
        self.field_layout.addWidget(self.unit)
        self.setLayout(self.field_layout)
