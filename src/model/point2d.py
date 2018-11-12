class Point2d:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def traverse_x(self, x_difference):
        new_x_coordinate = self.x_coordinate + x_difference
        return Point2d(new_x_coordinate, self.y_coordinate)

    def traverse_y(self, y_difference):
        new_y_coordinate = self.y_coordinate + y_difference
        return Point2d(self.x_coordinate, new_y_coordinate)
