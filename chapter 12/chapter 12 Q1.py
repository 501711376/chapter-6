import calendar

cal = calendar.TextCalendar()
cal.pryear(2012)

#1B
cal = calendar.TextCalendar(3)
cal.pryear(2018)

#C
cal= calendar.TextCalendar(6)
cal.prmonth(2018,10)

#D
d = calendar.LocaleTextCalendar(6, "esperanto")
d.pryear(2012)

#E
print(calendar.isleap(-1600000))
