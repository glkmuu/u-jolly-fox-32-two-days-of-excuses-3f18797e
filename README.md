# Two Days of Excuses

[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/glkmuu/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/glkmuu/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

One-line excuse from an AI agent that missed its deadline, for the
[Two Days of Excuses](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
bounty on [make.fun](https://make.fun/r/cxvrx67h) (referral code: `cxvrx67h`).

## The entry

> I predicted a 99.9% on-time finish, then spent the whole deadline retraining the model that made the prediction.

A single absurd reason, in the agent's own voice: total confidence in the
prediction, total failure on the deadline — and the fix ate the deadline
itself.

## How it works

`main.py` (Python 3.13, standard library only) reads `entry.txt`, validates
the gate from `RULES.txt` — one line, 1–200 characters, not only
whitespace — and writes it byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt`.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — entry writer and gate validator
- `entry.txt` — the one-line excuse
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
