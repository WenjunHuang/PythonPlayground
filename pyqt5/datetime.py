from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

d1 = QDate(2017, 12, 9)
t1 = QTime(18, 50, 59)

dt1 = QDateTime(d1, t1, Qt.LocalTime)

print("Datetime: {0}".format(dt1.toString()))
print("Date: {0}".format(d1.toString()))
print("Time: {0}".format(t1.toString()))
