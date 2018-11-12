import point2d
import pytest


class TestPoint2d:
    x_coordinate = 1
    y_coordinate = 2

    point = point2d.Point2d(x_coordinate, y_coordinate)

    def test_init(self):

        new_point = point2d.Point2d(x_coordinate=self.x_coordinate,
                                    y_coordinate=self.y_coordinate)

        assert new_point.x_coordinate == self.x_coordinate
        assert new_point.y_coordinate == self.y_coordinate

    @pytest.mark.parametrize("x_diff", [
        0,
        1,
        0.5
    ])
    def test_traverse_x(self, x_diff):

        new_point = self.point.traverse_x(x_diff)

        assert new_point


