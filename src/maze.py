from cell import Cell
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()
    
    def _create_cells(self):
        self._cells = [[Cell(self.win) for j in range(self.num_rows)] for i in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self,i,j):
        if self.win is None:
            return
        
        top_left_x = i * self.cell_size_x + self.x1
        top_left_y = j * self.cell_size_y + self.y1
        bottom_right_x = (i+1) * self.cell_size_x + self.x1
        bottom_right_y = (j+1) * self.cell_size_y + self.y1


        self._cells[i][j]._x1 = top_left_x
        self._cells[i][j]._y1 = top_left_y
        self._cells[i][j]._x2 = bottom_right_x
        self._cells[i][j]._y2 = bottom_right_y

        self._cells[i][j].draw()

        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

