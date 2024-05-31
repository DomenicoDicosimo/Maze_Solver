from point import Point
from line import Line

class Cell():
    def __init__(self,
                 _x1,_x2,_y1,_y2,
                 _win,
                 has_left_wall = True,
                 has_right_wall = True,
                 has_top_wall = True,
                 has_bottom_wall = True):
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win
    
    def draw(self):
        top_left_point = Point(self._x1,self._y1)
        bottom_left_point = Point(self._x1,self._y2)
        top_right_point = Point(self._x2,self._y1)
        bottom_right_point = Point(self._x2,self._y2)

        if self.has_left_wall is True:
            left_line = Line(top_left_point,bottom_left_point)
            self._win.draw_line(left_line,"blue")
        
        if self.has_right_wall is True:
            right_line = Line(top_right_point,bottom_right_point)
            self._win.draw_line(right_line,"Blue")

        if self.has_top_wall is True:
            top_line = Line(top_left_point,top_right_point)
            self._win.draw_line(top_line,"Blue")
        
        if self.has_bottom_wall is True:
            bottom_line = Line(bottom_left_point,bottom_right_point)
            self._win.draw_line(bottom_line,"Blue")

    def draw_move(self, to_cell, undo=False):
        color = "grey"
        if not undo:
            color = "red"
        init_cell_center_x = (self._x2 + self._x1) // 2
        init_cell_center_y = (self._y1 + self._y2) // 2
        to_cell_center_x = (to_cell._x2 + to_cell._x1) // 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) // 2
        
        print(init_cell_center_x)
        print(init_cell_center_y)
        print(to_cell_center_x)
        print(to_cell_center_y)

        init_cell_center_point = Point(init_cell_center_x,init_cell_center_y)
        to_cell_center_point = Point(to_cell_center_x,to_cell_center_y)

        center_line = Line(init_cell_center_point,to_cell_center_point)
        self._win.draw_line(center_line,color)