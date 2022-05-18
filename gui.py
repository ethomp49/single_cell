from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QTabBar, QPushButton, \
    QLabel, QGridLayout, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDoubleValidator, QIntValidator, QValidator


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
        # ---------------------------------------Current Data Window---------------------------------------------------

        self.current_data_window = QWidget()
        self.current_data_layout = QVBoxLayout()
        self.current_data_window.setLayout(self.current_data_layout)

        # ----Chart----

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
        self.data_chart_view = QChartView()
        self.data_chart_view.setChart(self.data_chart)
        self.current_data_layout.addWidget(self.data_chart_view)

        # ---- Import ----

        self.import_ribbon = QWidget()
        self.import_layout = QHBoxLayout()
        self.import_ribbon.setLayout(self.import_layout)

        self.import_button = QPushButton("Import data")
        self.import_button.setFixedWidth(100)
        self.import_layout.addWidget(self.import_button)

        self.import_text = QLabel("No data selected")
        self.import_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.import_layout.addWidget(self.import_text)
        self.current_data_layout.addWidget(self.import_ribbon)

        # ---- Parameters ----
        self.int_validator = QIntValidator()
        self.double_validator = QDoubleValidator()

        self.params = QWidget()
        self.params_layout = QGridLayout()
        self.params.setLayout(self.params_layout)

        self.stock_input = ParamField("Stock Concentration", self.double_validator, "particles/µL")
        self.dilution_input = ParamField("Dilution Factor", self.double_validator, "X")
        self.efficiency_input = ParamField("Transport Efficiency", self.double_validator, "%")
        self.sigma_input = ParamField("Sigma", self.int_validator, "")
        self.background_input = ParamField("Background Cutoff", self.int_validator, "counts")
        self.dwell_time_input = ParamField("Dwell Time", self.double_validator, "ms")

        self.params_layout.addWidget(self.stock_input, 0, 0)
        self.params_layout.addWidget(self.dilution_input, 1, 0)
        self.params_layout.addWidget(self.efficiency_input, 2, 0)
        self.params_layout.addWidget(self.sigma_input, 0, 1)
        self.params_layout.addWidget(self.background_input, 1, 1)
        self.params_layout.addWidget(self.dwell_time_input, 2, 1)

        self.current_data_layout.addWidget(self.params)

        # ---- Sample Info ----

        self.info_table = QTableWidget()

        self.info_table.setRowCount(1)
        self.info_table.setColumnCount(8)
        self.info_table.setHorizontalHeaderLabels(
            ['Particles Expected', 'Particles Counted', 'Max Signal(counts)', 'Min Signal(counts)',
             'Average Signal (counts)', 'Standard Deviation (counts)', 'Sigma', 'Background Cutoff (counts)'])
        self.info_table.resizeColumnsToContents()
        self.info_table.setFixedHeight(55)
        self.info_table.verticalHeader().setVisible(False)
        self.info_table.horizontalHeader().setSectionsClickable(False)
        self.info_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        for col in range(0, self.info_table.columnCount()):
            blank_item = QTableWidgetItem()
            blank_item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.info_table.setItem(0, col, blank_item)

        self.current_data_layout.addWidget(self.info_table)

        # ---- Collection Ribbon ----

        self.collection_ribbon = QWidget()
        self.collection_layout = QHBoxLayout()
        self.sample_label_label = QLabel("Sample Label")
        self.sample_label_label.setFixedWidth(70)
        self.sample_label_field = QLineEdit()
        self.collect_button = QPushButton("Save Data To Table")
        self.collect_button.setFixedWidth(150)

        for widget in [self.sample_label_label, self.sample_label_field, self.collect_button]:
            self.collection_layout.addWidget(widget)
        self.collection_ribbon.setLayout(self.collection_layout)

        self.current_data_layout.addWidget(self.collection_ribbon)

        # ----------------------------------------Histogram Window-----------------------------------------------------

        self.histogram_window = QWidget()

        # ----------------------------------Consecutive Particles Window-----------------------------------------------

        self.consecutive_particles_window = QWidget()

        # --------------------------------------Particle Data Window---------------------------------------------------

        self.corrected_particle_data_window = QWidget()

        self.collected_data_window = QWidget()

        stack_widgets = [self.current_data_window, self.histogram_window, self.consecutive_particles_window,
                         self.corrected_particle_data_window, self.collected_data_window]
        for widget in stack_widgets:
            self.stack.addWidget(widget)

        self.main_layout.addWidget(self.stack)

        self.show()

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

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.field)
        self.layout.addWidget(self.unit)
        self.setLayout(self.layout)
