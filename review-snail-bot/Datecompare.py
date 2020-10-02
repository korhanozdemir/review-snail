def dateBeautify(date):
    try:
        b = date.split(",")
        c = b[0].split(" ")
        d=int(b[-1])
        m=c[-2]
        y=int(c[-1])

        if m == 'January':
            m=1
        elif m == 'February':
            m=2
        elif m == 'March':
            m = 3
        elif m == 'April':
            m = 4
        elif m == 'May':
            m = 5
        elif m == 'June':
            m = 6
        elif m == 'July':
            m = 7
        elif m == 'August':
            m = 8
        elif m == 'September':
            m = 9
        elif m == 'October':
            m = 10
        elif m == 'November':
            m = 11
        elif m == 'December':
            m=12

        date = (d,m,y)
        return date

    except (IndexError,ValueError):
        return date


def dateComparison(date1,date2):
    try:
        if (date1 or date2) == 'no review yet':
            return False
        if date1>date2:
            return True
        if date2>=date1:
            return False
    except TypeError:
        return False

