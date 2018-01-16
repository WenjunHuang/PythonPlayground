from PyQt5.QtCore import QDate

xmas1 = QDate(2017, 1, 28)
xmas2 = QDate(2018, 2, 16)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print("{0} days have passed since last Spring Festival".format(dayspassed))

nofdays = now.daysTo(xmas2)
print("There are {0} days until next Spring Festival".format(nofdays))
