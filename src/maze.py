from cell import Cell
import time
import random

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
            seed = None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        if seed != None:
            random.seed(seed)

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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0,0)

        self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_walls_r(self,i,j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while True is True:
            valid_moves = []
            for di,dj in directions:
                new_i = i + di
                new_j = j + dj
            if 0 <= new_i < self.num_rows - 1 and 0 <= new_j < self.num_cols - 1:
                if not self._cells[new_i][new_j].visited:
                    valid_moves.append((new_i,new_j))
            
            if not valid_moves:
                self._draw_cell[i][j]
                return
            
            index = random.randrange(len(valid_moves))
            chosen_move =valid_moves[index]
            new_i,new_j = chosen_move
            
            
