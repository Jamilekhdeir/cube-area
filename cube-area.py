"""
Find the area of various geometric shapes
Wikipedia reference: https://en.wikipedia.org/wiki/Area
"""

from math import pi, sqrt, tan


def surface_area_cube(side_length: float) -> float:

    if side_length < 0:
        raise ValueError("surface_area_cube() only accepts non-negative values")
    return 6 * side_length**2


print(surface_area_cube(1))