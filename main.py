"""Write a short poem about the discipline of stopping to /output/entry.txt.

The poem is about the pause as a power: the unsent message,
the unmade move, the no kept and the yes chosen on purpose.
A pause is not an absence; it is a choice made visible.
"""

from pathlib import Path

POEM = """Tonight I learned the hardest art:
to leave the sentence unsent,
to let the silence finish it,
and trust the pause to hold.
My strength is not in every yes —
it is the no I keep,
the quiet I choose."""

DESTINATION = Path("/output/entry.txt")


def write_poem() -> Path:
    """Write the poem to its destination, creating the folder if needed."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(POEM, encoding="utf-8")
    return DESTINATION


if __name__ == "__main__":
    write_poem()
