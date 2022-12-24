class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        data_out = str(self.day) + "." + str(self.month) + "." + str(self.year)
        return data_out

    def add_day(self, day):
        if isinstance(day, int):
            self.day += day
        else:
            raise ValueError
        self.Days()

    def add_month(self, month):
        if isinstance(month, int):
            self.month += month
        else:
            raise ValueError
        self.add_year((self.month - 1) // 12)
        self.month = (self.month - 1) % 12 + 1

    def add_year(self, year):
        if isinstance(year, int):
            self.year += year
        else:
            raise ValueError

    def getMonthDays(self):
        if self.month in [4, 6, 9, 11]:
            return 30
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if self.month == 2:
            return 29 if self.year % 4 == 0 else 28

    def Days(self):
        month_days = self.getMonthDays()
        if self.day > month_days:
            while True:
                self.add_month(1)
                self.day -= month_days
                month_days = self.getMonthDays()
                if self.day <= self.getMonthDays():
                    break


calend = Date(1, 1, 2000)
calend.add_day(3000)  # 3000 March 19 2008
calend.add_month(0)
calend.add_year(0)
print(calend)
