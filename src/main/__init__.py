def checkIfYearIsLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return "Year is leap"
    elif year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return "Year is leap"
        else:
            return "Year is not leap"
    else:
        return "Year is not leap"
