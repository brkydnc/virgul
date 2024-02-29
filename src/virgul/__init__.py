from __virgul_cffi import ffi, lib

def number_of_floats_between(start: float, end: float) -> int:
    """Returns the number of NORMAL floating point numbers in range [`start`, `end`)."""

    assert a >= 0, "Both ends of the range (`start`, `end`) must be >= 0."
    assert b > a, "`end` must be greater than `start`"

    return lib.f32cnt(start, end)
