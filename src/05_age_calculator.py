import datetime
from dateutil import relativedelta


def run(y, m, d):
    today = datetime.datetime.now().date()
    birth_date = datetime.date(y, m, d)

    delta = relativedelta.relativedelta(today, birth_date)
    print(
        f"You have lived {delta.years} years, {delta.months} months and {delta.days} days.")


if __name__ == "__main__":
    YEAR = int(input("TYPE YOUR YEAR OF BIRTH:\t"))
    MONTH = int(input("TYPE YOUR MONTH OF BIRTH:\t"))
    DAY = int(input("TYPE YOUR DAY OF BIRTH:\t"))
    run(YEAR, MONTH, DAY)
