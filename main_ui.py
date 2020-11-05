import sys

from PyQt5.QtWidgets import QApplication
from ui.gui_test_result import TestResultWindow


if __name__ == '__main__':
    app = QApplication([])

    try:
        window = TestResultWindow()
        window.show()

        sys.exit(app.exec_())
    except Exception as exc:
        print(exc)
