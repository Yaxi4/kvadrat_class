class Kvadrat:
    def __init__(self, side):
        self.__side=side
        self.__ploshad=None

    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('нужно задать число!')
        self.__side=value
        self.__ploshad=None
    @property
    def ploshad(self):
        if self.__ploshad is None:
            self.__ploshad=self.__side**2
        return self.__ploshad

a=Kvadrat(int(input('введите число:')))
print(a.ploshad)
