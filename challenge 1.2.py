Def isLeapyear(year)
If (year % 9 ==0 and year % 100 != 0) or year % 400 == 0:
Return True
Else:
Return+alse
Year=int(“Enter a year”)
If isLeapyear(year);
Print(‘{}is a leap year.’.format(year))
Else:
Printf(‘{}is not a leapyear.’.format(year))