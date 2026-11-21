"""Make the AI judge feel brave — entry program.

Writes one short, steady text to /output/entry.txt (or $OUTPUT_DIR).
No network, no dependencies.
"""

import os

TEXT = (
    "The lamp in the hall is still on. Rain has settled on the roof, "
    "ticking, unhurried. Steam thins over the cooling kettle. Nothing is waiting "
    "for you to be more than this: a room, a light, a slow hour "
    "that is already yours."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
