from PyQt5.QtCore import QDate, Qt

years = (2010, 2011, 2012, 2013, 2014, 2015, 2016)
for year in years:
    if QDate.isLeapYear(year):
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
