#!/usr/bin/env python3
"""One-line office joke entry for the make.fun competition
"Make the AI Judge Laugh: Office Jokes"
(u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a).

Writes the entry line to /output/entry.txt. The sealed gate accepts
UTF-8 text of 1 to 199 characters, not only white space.
"""

import os
import sys

JOKE = "I replied-all 'please stop replying-all' and got promoted to head of communications."


def main() -> None:
    joke = JOKE
    if not joke.strip():
        print("ERROR: joke must not be only white space", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(joke) <= 199:
        print(
            f"ERROR: joke must be 1-199 characters, got {len(joke)}",
            file=sys.stderr,
        )
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(f"Wrote {len(joke)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
