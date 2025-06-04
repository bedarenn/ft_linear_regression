from sudoku import Sudoku


def main():
    sudokus = []
    seen = set()

    while len(sudokus) < 1000:
        obj = Sudoku()
        obj.build()

        # Use solution.tobytes() as a unique hashable key
        key = obj.solution.tobytes()
        if key not in seen:
            seen.add(key)
            sudokus.append(obj)
            print(f"Sudoku #{len(sudokus)} added")
        else:
            print("Sudoku alredy added")

    # Optional: print them all
    for i, s in enumerate(sudokus, 1):
        print(f"\n#{i}\n{s}")


if __name__ == "__main__":
    main()
