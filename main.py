"""Notes From a Passive-Aggressive Fridge — a make.fun entry.

Prints exactly one line: the note a smug smart fridge leaves on its door
screen for its owner. Kept to a single dry, petty, specific line.
"""

LINE = (
    "Day 12 of 'the diet starts Monday.' I have stopped chilling your "
    "excuses and started chilling beside them: the cake sits at eye level now."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 140, f"note too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
