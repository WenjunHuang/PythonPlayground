from PyQt5.QtCore import QDate, QLocale

now = QDate.currentDate()
dayOfWeek = now.dayOfWeek()
print(QDate.shortDayName(dayOfWeek))
print(QDate.longDayName(dayOfWeek))

locale = QLocale(QLocale.Chinese, QLocale.China)
print(locale.toString(now, 'dddd'))
