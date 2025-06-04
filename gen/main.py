from sudoku import Sudoku

def main():
    obj = Sudoku()
    obj.build()
    print(obj.__str__())

if __name__ == "__main__":
    main()