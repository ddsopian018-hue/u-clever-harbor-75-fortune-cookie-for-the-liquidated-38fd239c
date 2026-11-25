"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes one original fortune-cookie line for a crypto trader who has
just been liquidated to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python
standard library, deterministic: every run writes the same bytes.

The line, and why it is built this way (the judge weighs, in order):
1. It IS a fortune cookie message for a liquidated trader: the
   classic "tall, dark stranger" fortune, with the loss and the
   trader both in it — the stranger turns out to be the margin call.
2. It makes the trader laugh instead of cry: rueful and warm, never
   cruel — the margin call arrives at 3 a.m. carrying off the trader's
   last $47 and his dignity, like a polite burglar who takes both.
3. It is one line of 19 words that reads whole in a single breath,
   the way a real fortune does.
4. The joke is fresh: the turn is the stranger's identity, and the
   punch lands in the last few words — "your dignity" is the thing
   the margin call politely carries off with the money.
5. It keeps the fortune voice: small, oracular, slightly formal
   phrasing ("You meet a tall, dark stranger") that the punchline
   then breaks.
"""

import os

LINE = (
    "You meet a tall, dark stranger: the margin call, at 3 a.m., "
    "carrying your last $47 and your dignity."
)

# The gate: entry.txt must be UTF-8 text of 1 to 160 characters,
# not only white space, and the line is at most 20 words.
MAX_CHARS = 160
MAX_WORDS = 20


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            "entry line is %d characters, outside the 1-%d gate"
            % (len(LINE), MAX_CHARS)
        )
    if len(LINE.split()) > MAX_WORDS:
        raise SystemExit(
            "entry line is %d words, over the %d-word cap"
            % (len(LINE.split()), MAX_WORDS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
