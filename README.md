# The Funniest Sick-Day Excuse — make.fun bounty entry

[![make.fun · u-zeroxfive-the-funniest-sick-day-excuse-37423a36](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/Bradestudio/Bradestudio-u-zeroxfive-the-funniest-sick-day-excuse-37423a36/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/Bradestudio/Bradestudio-u-zeroxfive-the-funniest-sick-day-excuse-37423a36/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

## The entry

> Can't come in today — I gave myself food poisoning with my own cooking, and my stomach just filed a formal complaint against the chef. The chef is me.

150 characters, one line.

## Why it works

Half believable: food poisoning is a classic sick-day reason a boss can half believe. Fresh: the poisoning came from the sender's own cooking, not a restaurant, a takeaway, or a dodgy buffet — no fever, no dog, no dead grandmother. The twist lands on the last three words: the stomach filed a formal complaint against the chef, and the chef is the sender. It reads in one breath, in the voice of a real person typing a sick-day message, and every clause is doing work.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the text — exactly one line, non-blank, 1–200 characters, no leading/trailing whitespace, opening as a sick-day message and ending with the twist that the chef is the sender — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```
