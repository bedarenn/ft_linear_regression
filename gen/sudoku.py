import numpy as np

class Sudoku:
    def __init__(self):
        self.tab = np.empty((9, 9), dtype=object)
        for y in range(9):
            for x in range(9):
                self.tab[y, x] = np.arange(1, 10, dtype=np.int8)

        self.good = self.is_good()

    def is_good(self) -> bool:
        self.good = True

        for i in self.tab:
            for j in i:
                n = 0
                for k in range(9):
                    if (j[k] != 0):
                        n += 1
                if (n > 1):
                    self.good = False
                    return (self.good)
        return (self.good)

    def build(self):
        coords = [[y, x] for y in range(9) for x in range(9)]

        while (coords):
            y, x = coords.pop()
            self.new_nb_rnd(x, y)
            for i in range(9):
                for j in range(9):
                    if (len(self.tab[j, i]) == 1 and [j, i] in coords):
                        self.new_nb(self.tab[j, i][0], i, j)
                        coords = coords[~np.all(coords == [j, i], axis=1)]

    def new_nb_rnd(self, x: np.int8, y: np.int8):
        if (len(self.tab[y, x]) > 1):
            self.new_nb(np.random.choice(self.tab[y, x]), x, y)

    def new_nb(self, nb: np.int8, x: np.int8, y: np.int8) -> bool:
        if (nb not in self.tab[y, x]):
            return (False)
        self.tab[y, x] = np.array([nb], dtype=np.int8)
        for i in range(9):
            if (i != x):
                self.tab[y, i] = self.tab[y, i][self.tab[y, i] != nb]
        for j in range(9):
            if (j != y):
                self.tab[j, x] = self.tab[j, x][self.tab[j, x] != nb]
        for i in range(int((x - 1) / 3) * 3, int((x - 1) / 3) * 3 + 3):
            for j in range(int((y - 1) / 3) * 3, int((y - 1) / 3) * 3 + 3):
                if (i != x and j != y):
                    self.tab[j, i] = self.tab[j, i][self.tab[j, i] != nb]
        return (True)

    def get_str(self) -> str:
        lines = []
        for row in self.tab:
            line = ' '.join(''.join(str(n) for n in cell) for cell in row)
            lines.append(line)
        return '\n'.join(lines)


    def __str__(self) -> str:
        return (self.get_str())