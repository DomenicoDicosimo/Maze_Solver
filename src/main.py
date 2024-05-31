from window import Window
from point import Point
from line import Line
from cell import Cell


def main():
    win = Window(800,600)
    
    cell1 = Cell(10,70,70,10,win,True,True,False,True)
    cell1.draw()

    cell2 = Cell(10,70,130,70,win,True,True,True,False)
    cell2.draw()

    cell1.draw_move(cell2,True)

    

    win.wait_for_close()

    

main()