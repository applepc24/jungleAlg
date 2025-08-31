def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

days_in_month = [31, 28, 31, 30, 31, 30, 31,
                 31, 30, 31, 30, 31]

def count_days_until(y1, m1, d1, y2, m2, d2):
    def date_to_days(y, m, d):
        days = d
        for year in range(1, y):
            if leap_year(year):
                days += 366
            else:
                days += 365
        for month in range(1, m):
            if month ==2 and leap_year(y):
                days += 29
            else:
                days += days_in_month[month -1]
        return days
    return date_to_days(y2, m2, d2) - date_to_days(y1, m1, d1)

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if y2 >= y1 + 1000 or (y2 == y1 + 1000 and (m2, d2) >= (m1, d1)):
    print('gg')
else:
    answer = count_days_until(y1, m1, d1, y2, m2, d2)
    print(f"D-{answer}")
