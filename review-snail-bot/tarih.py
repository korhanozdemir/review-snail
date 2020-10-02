def dateBeautify(date):
    try:
        b = date.split(" ")
        m=b[1]
        d=int(b[0])
        y=int(b[2])

        if m == 'Ocak':
            m=1
        elif m == 'Şubat':
            m=2
        elif m == 'Mart':
            m = 3
        elif m == 'Nisan':
            m = 4
        elif m == 'Mayıs':
            m = 5
        elif m == 'Haziran':
            m = 6
        elif m == 'Temmuz':
            m = 7
        elif m == 'Ağustos':
            m = 8
        elif m == 'Eylül':
            m = 9
        elif m == 'Ekim':
            m = 10
        elif m == 'Kasım':
            m = 11
        elif m == 'Aralık':
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


