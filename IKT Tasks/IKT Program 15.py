class Students:
    _students = []

    def __init__(self, name, year, month, day, sinif):
        self.name = name
        self.year = year
        self.month = month
        self.day = day
        self.sinif = sinif
        self._append()

    def _append(self):
        self._students.append(self.name.title())

    @classmethod
    def show(cls):
        return cls._students.copy()

    @classmethod
    def now(cls, name, date, sinif):
        date = date.split('/')
        return cls(name, date[0], date[1], date[2], sinif)

    def __str__(self):
        return f"{self.name} = Students('{self.name}')"


rufet = Students('hikmet', '1992', '03', '03', '1s')
hikmet = Students.now('hikmet', '1992/03/04', '1s')

print(hikmet.year)
print(rufet.year)