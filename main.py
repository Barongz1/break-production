"""Break Production, Own It — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the one line an AI agent prints the moment it breaks production, under 200 characters.
"""
import os

LINE = "Root cause: me. I pushed to production on Friday at 4:59 PM, because all the tests passed on my machine."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
