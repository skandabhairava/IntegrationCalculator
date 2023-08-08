import math

class Squareroot:
    def __init__(self, item) -> None:
        self.items = []

        if isinstance(item, int|float):
            if item < 0:
                return

            try:
                res = math.sqrt(item)
                self.items.extend([res, -res])
            except ValueError:
                ... #its out of range
        elif isinstance(item, Squareroot):
            for i in item.items:
                res = Squareroot(i)
                self.items.extend(res.items)

    def append(self, other, lis: list):
        if other in lis:
            return

        lis.append(other)

    def __add__(self, other):
        lis = []
        for i in self.items:
            self.append(i + other, lis)

        self.items = lis
        return self

    def __sub__(self, other):
        lis = []
        for i in self.items:
            self.append(i - other, lis)

        self.items = lis
        return self

    def __mul__(self, other):
        lis = []
        for i in self.items:
            self.append(i * other, lis)

        self.items = lis
        return self

    def __truediv__(self, other):
        lis = []
        for i in self.items:
            self.append(i / other, lis)

        self.items = lis
        return self

    def __pow__(self, other):
        lis = []
        for i in self.items:
            self.append(i ** other, lis)

        self.items = lis
        return self

    def __repr__(self) -> str:
        return str(self.items)
