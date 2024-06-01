import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create__zero_cells(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,None)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_test_visited(self):
        visit = False
        m1 = Maze(0, 0, 10, 10, 10, 10,None)
        m1._create_cells()
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        m1._reset_cells_visited()
        self.assertEqual(
            m1._cells[0][0].visited,
            visit,
        )

if __name__ == "__main__":
    unittest.main()

