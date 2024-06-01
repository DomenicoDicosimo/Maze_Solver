from window import Window
from maze import Maze


def main():
    win = Window(800,800)
    
    maze = Maze(5,5,10,10,20,20,win)

    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    
    win.wait_for_close()

    

main()