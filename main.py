import argparse
from grid import Grid
from solver import BackwardSolver

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default="", type=str,
                        help='path to a board file')

    parser.add_argument('--steps', default=1000,
                        type=int, help='number of steps')
    arguments = parser.parse_args()
    if arguments.file != "":
        grid = Grid.from_file(arguments.file)
        solver = BackwardSolver(grid)
#        solver.solve()
#        print(grid.grid)
        solver.debug = False
        solver.solve()
        grid.show()
#        while not solver.solved:
#            solver.step()
#            grid.show()
#            a = input()
#        print("solved")
