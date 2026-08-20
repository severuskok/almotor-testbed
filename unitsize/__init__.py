"""Human readable byte sizes, both directions.

    >>> human_size(2500)
    '2.4 KB'
    >>> parse_size("2.4 KB")
    2458
"""

from __future__ import annotations

__all__ = ["human_size", "parse_size", "UNITS", "STEP"]

__version__ = "0.2.0"

UNITS = ["B", "KB", "MB", "GB", "TB", "PB"]
STEP = 1024


def human_size(num_bytes: int, precision: int = 1) -> str:
    """Format a byte count the way a file manager would.

    Bytes are printed whole, because "1.0 B" helps nobody. Everything above
    that gets `precision` decimals.
    """
    if num_bytes < 0:
        raise ValueError("num_bytes must not be negative")

    size = float(num_bytes)
    unit = 0
    # Step up while the value still fills a whole unit. This has to be >=, not
    # >, so that exactly STEP bytes rolls over: 1024 is 1.0 KB, not 1024 B, and
    # 1024 KB is 1.0 MB, not 1024.0 KB.
    while size >= STEP and unit < len(UNITS) - 1:
        size /= STEP
        unit += 1

    if unit == 0:
        return f"{int(size)} {UNITS[unit]}"
    return f"{size:.{precision}f} {UNITS[unit]}"


def parse_size(text: str) -> int:
    """Turn "2.4 KB" back into a whole number of bytes.

    The unit is optional and case insensitive; a bare number is bytes.
    """
    cleaned = (text or "").strip()
    if not cleaned:
        raise ValueError("nothing to parse")

    digits = ""
    for index, char in enumerate(cleaned):
        if char.isdigit() or char in ".-+":
            digits += char
        else:
            break
    if not digits:
        raise ValueError(f"no number in {text!r}")

    suffix = cleaned[len(digits):].strip().upper() or "B"
    if suffix not in UNITS:
        raise ValueError(f"unknown unit {suffix!r}")

    return int(round(float(digits) * STEP ** UNITS.index(suffix)))
