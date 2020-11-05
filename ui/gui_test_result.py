import requests
import json

from .gui_raw.gui_test_result_template import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem


class TestResultWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(TestResultWindow, self).__init__(parent)
        self.setupUi(self)

        header = self.test_result_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        self.search_button.clicked.connect(self.get_stats)
        self.search_input.returnPressed.connect(self.get_stats)

        self.add_record_button.clicked.connect(self.add_record)
        self.add_record_operator_input.returnPressed.connect(self.add_record)

        self.delete_record_button.clicked.connect(self.delete_record)
        self.delete_record_input.returnPressed.connect(self.delete_record)

    def get_stats(self):
        try:
            r = requests.get(f'http://127.0.0.1:5000/api_v1/stat/?operator={self.search_input.text()}')
            data = json.loads(r.content)
        except Exception as exc:
            print(exc)
            data = []

        self.test_result_table.setRowCount(0)
        for i, record in enumerate(data):
            self.test_result_table.setRowCount(i + 1)
            self.test_result_table.setItem(i, 0, QTableWidgetItem(record['device_type']))
            self.test_result_table.setItem(i, 1, QTableWidgetItem(str(record['total_tests'])))
            self.test_result_table.setItem(i, 2, QTableWidgetItem(str(record['successes'])))
            self.test_result_table.setItem(i, 3, QTableWidgetItem(str(record['failures'])))
            self.test_result_table.setRowHeight(i, 10)

    def add_record(self):
        device = self.add_record_device_input.text()
        operator = self.add_record_operator_input.text()
        result = int(self.add_record_result_box.currentText() == 'Успішно')

        try:
            requests.post('http://127.0.0.1:5000/api_v1/test_result/', json={'device_type': device,
                                                                         'operator': operator,
                                                                         'success': result})
        except Exception as exc:
            print(exc)

        self.get_stats()  # update stats

    def delete_record(self):
        record_id = self.delete_record_input.text()

        try:
            requests.delete(f'http://127.0.0.1:5000/api_v1/test_result/{record_id}')
        except Exception as exc:
            print(exc)

        self.get_stats()  # update stats
