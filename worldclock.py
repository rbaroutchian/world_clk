from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from datetime import datetime
import pytz
import sys
from clock import Ui_world_clock  # وارد کردن فایل تولید شده از Qt Designer

class TimeApp(QtWidgets.QMainWindow, Ui_world_clock):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # غیرقابل ویرایش کردن تمام QTimeEdit ها
        self.timeEdit.setReadOnly(True)
        self.timeEdit_2.setReadOnly(True)
        self.timeEdit_3.setReadOnly(True)
        self.timeEdit_4.setReadOnly(True)
        self.timeEdit_5.setReadOnly(True)

        # اتصال دکمه به متد بروزرسانی زمان
        self.update_button.clicked.connect(self.update_time)

        # تنظیم تایمر برای بروزرسانی زمان هر ثانیه (در صورت نیاز)
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_time)
        # self.timer.start(1000)  # بروزرسانی هر 1 ثانیه

        self.timezones = {
            'Iran': 'Asia/Tehran',
            'USA': 'America/New_York',
            'UK': 'Europe/London',
            'Japan': 'Asia/Tokyo',
            'Australia': 'Australia/Sydney'
        }

        self.update_time()

    def update_time(self):
        # بروزرسانی ساعت در هر QTimeEdit
        self.update_timeedit(self.timeEdit, 'Iran')
        self.update_timeedit(self.timeEdit_2, 'USA')
        self.update_timeedit(self.timeEdit_3, 'UK')
        self.update_timeedit(self.timeEdit_4, 'Japan')
        self.update_timeedit(self.timeEdit_5, 'Australia')

    def update_timeedit(self, time_edit, country):
        tz = pytz.timezone(self.timezones[country])
        country_time = datetime.now(tz)
        time_edit.setTime(QtCore.QTime(country_time.hour, country_time.minute, country_time.second))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TimeApp()
    window.show()
    sys.exit(app.exec_())
