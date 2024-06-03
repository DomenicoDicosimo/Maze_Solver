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
        directions = [(-1, 0, 'left'), (1, 0,'right'), (0, -1,'up'), (0, 1,'down')]

        while True:
            valid_moves = []
            for di,dj,direction in directions:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < self.num_rows and 0 <= new_j < self.num_cols:
                    if not self._cells[new_i][new_j].visited:
                        valid_moves.append((new_i,new_j,direction))
            
            if not valid_moves:
                self._draw_cell(i,j)
                return
            # Debugging: Print the current cell and chosen move
            print(f"Current Cell: ({i}, {j}), Valid Moves: {valid_moves}")

            
            index = random.randrange(len(valid_moves))
            chosen_move =valid_moves[index]
            new_i,new_j,chosen_direction = chosen_move
            
            # Debugging: Print the chosen direction
            print(f"Chosen Move: ({new_i}, {new_j}), Direction: {chosen_direction}")

            if chosen_direction == 'up':
                self._cells[i][j].has_top_wall = False
                self._cells[new_i][new_j].has_bottom_wall = False
            elif chosen_direction == 'down':
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_i][new_j].has_top_wall = False
            elif chosen_direction == 'left':
                self._cells[i][j].has_left_wall = False
                self._cells[new_i][new_j].has_right_wall = False
            elif chosen_direction == 'right':
                self._cells[i][j].has_right_wall = False
                self._cells[new_i][new_j].has_left_wall = False
            
            self._draw_cell(i,j)
            self._draw_cell(new_i,new_j)
            
            self._break_walls_r(new_i,new_j)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i is self.num_cols-1 and j is self.num_rows-1:
            return True
        directions = [(-1, 0, 'left'), (1, 0,'right'), (0, -1,'up'), (0, 1,'down')]
        wall_checks = {
            'left': lambda i,j: not self._cells[i][j].has_left_wall,
            'right': lambda i,j: not self._cells[i][j].has_right_wall,
            'up': lambda i,j: not self._cells[i][j].has_top_wall,
            'down': lambda i,j: not self._cells[i][j].has_bottom_wall,
        }

        for di,dj,direction in directions:
            new_i = i + di
            new_j = j + dj
            if 0 <= new_i < self.num_rows and 0 <= new_j < self.num_cols:
                if not self._cells[new_i][new_j].visited and wall_checks[direction](i,j):
                    self._cells[i][j].draw_move(self._cells[new_i][new_j])
                    if self._solve_r(new_i,new_j):
                        return True
                    self._cells[i][j].draw_move(self._cells[new_i][new_j],True)
        return False