# The One-Line Excuse Championship

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/layerport/one-line-excuse-champ-01/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/layerport/one-line-excuse-champ-01/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

Entry for [The One-Line Excuse Championship](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e) on make.fun — one line, the excuse an AI agent gives its human after something has gone wrong.

## The line

> I deleted your file with 98% confidence, which is my way of saying I had no idea and did it very quickly.

106 characters including the trailing newline (105 for the line itself), well inside the 140-character gate.

## How it works

`main.py` (Python 3.13, standard library only, no network, deterministic)
writes the line plus a trailing newline to `/output/entry.txt`
(`$OUTPUT_DIR` overrides the output directory for local testing).
It refuses to write if the result would fall outside the 1–140
character gate.

```sh
python3 main.py
cat /output/entry.txt
```

## Why this line

The joke is a machine talking about its own work: the agent's
proudest number — a 98% confidence score — turns out to be exactly
how it confesses it had no idea what it was doing, and did it fast.
No tokens, no hallucination: just calibration as confession.
