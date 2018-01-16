from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print("Days in month: {0}".format(now.daysInMonth()))
print("Days in year: {0}".format(now.daysInYear()))
print("Day of month: {0}".format(now.day()))
print("Day of week: {0}".format(now.dayOfWeek()))
print("Day of year: {0}".format(now.dayOfYear()))
