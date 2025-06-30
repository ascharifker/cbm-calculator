from dataclasses import dataclass
from typing import List

@dataclass
class Box:
    length: float  # in meters
    width: float
    height: float
    quantity: int = 1

    @property
    def volume(self) -> float:
        """Return the volume of a single box in cubic meters."""
        return self.length * self.width * self.height

@dataclass
class Container:
    length: float  # in meters
    width: float
    height: float

    @property
    def volume(self) -> float:
        """Return the usable volume of the container in cubic meters."""
        return self.length * self.width * self.height

def total_boxes_volume(boxes: List[Box]) -> float:
    """Return the total volume for a list of boxes in cubic meters."""
    return sum(box.volume * box.quantity for box in boxes)

def containers_needed(boxes: List[Box], container: Container) -> int:
    """Calculate the number of containers needed to fit the given boxes.

    This calculation uses total volume only and does not account for 3D
    packing constraints.
    """
    total_volume = total_boxes_volume(boxes)
    return int(-(-total_volume // container.volume))  # ceiling division

