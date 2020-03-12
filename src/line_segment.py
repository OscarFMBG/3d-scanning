from dataclasses import dataclass

from .vertex import Vertex


@dataclass
class LineSegment:
    __slots__ = ("origin", "direction", "magnitude")

    origin: Vertex
    direction: Vertex
    magnitude: float

    @property
    def end(self):
        return Vertex(
            self.origin.x + self.magnitude * self.direction.x,
            self.origin.y + self.magnitude * self.direction.y,
            self.origin.z + self.magnitude * self.direction.z,
        )
