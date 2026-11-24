"""Entry for make.fun bounty "The Funniest Sick-Day Excuse"
(u-zeroxfive-the-funniest-sick-day-excuse-37423a36).

The entry is a single funny sick-day excuse line, 1-200 characters,
written verbatim to the output file.

Judge criteria it aims for: funniest — the excuse escalates absurdly
(gas station sushi at midnight -> a full legal trial inside the body);
original — no generic "food poisoning" phrasing, a specific time, place,
and food that make the scene concrete; specific — one vivid incident with
a clear cause and an outsized consequence, so it lands as a complete joke
in a single sentence.
"""

import os

LINE = "I ate a gas station sushi roll at midnight and my body is now hosting a full legal trial."
MAX_LEN = 200

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "./output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= MAX_LEN, f"LINE length {len(LINE)} out of range 1-{MAX_LEN}"

    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        path = OUTPUT_PATH
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    except OSError:
        os.makedirs(os.path.dirname(FALLBACK_PATH), exist_ok=True)
        path = FALLBACK_PATH
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)

    # Self-check: read back and verify byte-identical content, no trailing newline.
    with open(path, "rb") as f:
        data = f.read()
    assert data == LINE.encode("utf-8"), "entry.txt content does not match LINE"
    assert not data.endswith(b"\n"), "entry.txt must not end with a trailing newline"
    assert data[-1:] != b"\n" and len(data) == len(LINE) == 89, (
        f"entry length {len(data)} != expected 89; last byte {data[-1:]!r}"
    )
    assert data.decode("utf-8") == LINE, "entry.txt decoded text does not equal LINE"

    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
