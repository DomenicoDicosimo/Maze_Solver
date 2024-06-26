from point import Point
from line import Line

class Cell():
    def __init__(self,
                 _win
                 ):
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = _win
        self.visited = False
    
    def draw(self):
        top_left_point = Point(self._x1,self._y1)
        bottom_left_point = Point(self._x1,self._y2)
        top_right_point = Point(self._x2,self._y1)
        bottom_right_point = Point(self._x2,self._y2)

        if self.has_left_wall is True:
            left_line = Line(top_left_point,bottom_left_point)
            self._win.draw_line(left_line,"blue")
        else:
            left_line = Line(top_left_point,bottom_left_point)
            self._win.draw_line(left_line,"white")
        
        if self.has_right_wall is True:
            right_line = Line(top_right_point,bottom_right_point)
            self._win.draw_line(right_line,"Blue")
        else:
            right_line = Line(top_right_point,bottom_right_point)
            self._win.draw_line(right_line,"white")

        if self.has_top_wall is True:
            top_line = Line(top_left_point,top_right_point)
            self._win.draw_line(top_line,"Blue")
        else:
            top_line = Line(top_left_point,top_right_point)
            self._win.draw_line(top_line,"white")
        
        if self.has_bottom_wall is True:
            bottom_line = Line(bottom_left_point,bottom_right_point)
            self._win.draw_line(bottom_line,"Blue")
        else:
            bottom_line = Line(bottom_left_point,bottom_right_point)
            self._win.draw_line(bottom_line,"white")

    def draw_move(self, to_cell, undo=False):
        color = "grey"
        if not undo:
            color = "red"
        init_cell_center_x = (self._x2 + self._x1) // 2
        init_cell_center_y = (self._y1 + self._y2) // 2
        to_cell_center_x = (to_cell._x2 + to_cell._x1) // 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) // 2

        init_cell_center_point = Point(init_cell_center_x,init_cell_center_y)
        to_cell_center_point = Point(to_cell_center_x,to_cell_center_y)

        center_line = Line(init_cell_center_point,to_cell_center_point)
        self._win.draw_line(center_line,color)