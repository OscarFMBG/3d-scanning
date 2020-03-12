from dataclasses import dataclass


@dataclass
class Vertex:
    __slots__ = ("x", "y", "z")

    x: float
    y: float
    z: float
