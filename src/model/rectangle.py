import point2d


class ParallelRectangle:

    def __init__(self, top_left_point, width, height):

        self.top_left_point = top_left_point
        self.width = width
        self.height = height


class TurnableRectangle(ParallelRectangle):

    def __init__(self, top_left_point, width, height, angle):

        super.__init__(top_left_point, width, height)
        self.angle = angle

    def get_top_right_point(self):
        pass

    def get_bottom_left_point(self):
        pass

    def get_bottom_right_point(self):
        pass

    def change_orientation_to_left(self):
        """
        Keeps rectangle in same place but changes orientation by 90 degrees to the left
        :return: a TurnableRectangle
        """
        new_hook_point = self.top_left_point
        new_angle = self.angle + 90 % 360
        return TurnableRectangle(top_left_point=new_hook_point,
                                 width=self.height,
                                 height=self.width,
                                 angle=new_angle)

    def change_orientation_to_back(self):
        return self.change_orientation_to_left().change_orientation_to_left()

    def change_orientation_to_right(self):
        return self.change_orientation_to_left().change_orientation_to_left().change_orientation_to_left()

    def turn_around_top_left(self, angle):
        new_angle = (self.angle + angle) % 360
        return TurnableRectangle(self.base_rectangle, new_angle)

    def turn_around_top_right(self, angle):

        temporary_rectangle = self.change_orientation_to_right()
        temporary_rectangle.turn_around_top_left(-angle)
        return temporary_rectangle.change_orientation_to_left()


if __name__ == "__main__":
    my_rectangle = ParallelRectangle(point2d.Point2d(10, 20), 100, 200)
    print(my_rectangle)

    my_turnable_rectangle = TurnableRectangle(my_rectangle, 30)

    print(my_turnable_rectangle.turn(360.5).angle)

