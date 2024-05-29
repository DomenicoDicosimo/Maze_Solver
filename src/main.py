from window import Window
from point import Point
from line import Line
from cell import Cell


def main():
    win = Window(800,600)
    
    cell1 = Cell(10,70,70,10,win,True,True,True,True)

    cell1.draw()

    win.wait_for_close()

    

main()