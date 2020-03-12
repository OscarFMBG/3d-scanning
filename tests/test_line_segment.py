from src.line_segment import LineSegment
from src.vertex import Vertex


def test_initalization():
    LineSegment(Vertex(1, 2, 3), Vertex(4, 5, 6), 3.2)


def test_end():
    line_segment = LineSegment(Vertex(0, 0, 0), Vertex(1, 1, 1), 3.5)
    assert line_segment.end == Vertex(3.5, 3.5, 3.5)
