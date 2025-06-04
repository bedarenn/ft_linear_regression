import numpy as np
import random
import copy


class Sudoku:
    def __init__(self):
        self.grid = np.zeros((9, 9), dtype=np.uint8)
        self.solution = None
        self.nb_soluce = 0

    def __str__(self):
        def format_grid(g):
            lines = []
            top = "┌" + "───────┬" * 2 + "───────┐"
            sep = "├" + "───────┼" * 2 + "───────┤"
            bot = "└" + "───────┴" * 2 + "───────┘"
            lines.append(top)
            for i, row in enumerate(g):
                line = "│ " + " │ ".join(
                    ' '.join(str(n) if n != 0 else '.' for n in row[j:j+3])
                    for j in range(0, 9, 3)
                ) + " │"
                lines.append(line)
                if i == 8:
                    lines.append(bot)
                elif (i + 1) % 3 == 0:
                    lines.append(sep)
            return '\n'.join(lines)

        return (
            f"Puzzle:\n{format_grid(self.grid)}\n\n"
            f"Solution:\n{format_grid(self.solution)}\n"
            f"nb_soluce: {self.nb_soluce}\n"
        )

    def is_valid(self, grid, row, col, num):
        if num in grid[row]:
            return False
        if num in grid[:, col]:
            return False
        y0, x0 = 3 * (row // 3), 3 * (col // 3)
        if num in grid[y0:y0+3, x0:x0+3]:
            return False
        return True

    def solve(self, grid):
        for y in range(9):
            for x in range(9):
                if grid[y, x] == 0:
                    for n in range(1, 10):
                        if self.is_valid(grid, y, x, n):
                            grid[y, x] = n
                            if self.solve(grid):
                                return True
                            grid[y, x] = 0
                    return False
        return True

    def fill_grid(self):
        nums = list(range(1, 10))
        for y in range(9):
            for x in range(9):
                if self.grid[y, x] == 0:
                    random.shuffle(nums)
                    for n in nums:
                        if self.is_valid(self.grid, y, x, n):
                            self.grid[y, x] = n
                            if self.fill_grid():
                                return True
                            self.grid[y, x] = 0
                    return False
        return True

    def build(self):
        self.fill_grid()
        self.solution = self.grid.copy()  # Save full filled solution

        coords = [(y, x) for y in range(9) for x in range(9)]
        random.shuffle(coords)

        for y, x in coords:
            backup = self.grid[y, x]
            self.grid[y, x] = 0

            grid_copy = self.grid.copy()
            if self.count_solutions(grid_copy, limit=2) != 1:
                self.grid[y, x] = backup  # Restore if not uniquely solvable
                break
        self.nb_soluce = self.count_solutions(self.grid)

    def count_solutions(self, grid, limit=2):
        self.solution_count = 0
        self._count_backtrack(grid, limit)
        return self.solution_count

    def _count_backtrack(self, grid, limit):
        for y in range(9):
            for x in range(9):
                if grid[y, x] == 0:
                    for n in range(1, 10):
                        if self.is_valid(grid, y, x, n):
                            grid[y, x] = n
                            self._count_backtrack(grid, limit)
                            grid[y, x] = 0
                            if self.solution_count >= limit:
                                return
                    return
        self.solution_count += 1

    def __eq__(self, other):
        if not isinstance(other, Sudoku):
            return NotImplemented
        return np.array_equal(self.solution, other.solution)
