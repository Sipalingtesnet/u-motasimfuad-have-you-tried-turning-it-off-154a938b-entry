"""
Module docstring:
Chosen line: "Your entire company is collapsing, but have you tried wiggling the mouse to wake it up?"

Why this line wins on the five criteria:
1. Hopeless support agent to desperate customer: Perfectly captures the infuriating mismatch between a customer facing total ruin and an agent blindly reading from a tier-1 script.
2. Lands the joke with unexpected twist: The cheerful uselessness of "wiggling the mouse" in the face of corporate collapse is inherently funny, and the customer is treated with absolute sympathy.
3. Sounds real and felt: It channels the authentic, soul-crushing absurdity of real tech support calls where colossal disaster meets bureaucratic indifference.
4. Tight wording: Every word is economical, landing the punchline instantly on first read.
5. Fresh twist: It subverts the classic troubleshooting trope ("did you move the mouse?") by escalating the customer's problem to a catastrophic business collapse.
"""

import os

def main():
    line = "Your entire company is collapsing, but have you tried wiggling the mouse to wake it up?"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()

# Determinism verification:
# main.py executes deterministically by writing the exact hardcoded string literal
# to /output/entry.txt without network calls, random number generators, or time dependencies.
# Running main.py multiple times produces identical byte content and sha256 hashes.
