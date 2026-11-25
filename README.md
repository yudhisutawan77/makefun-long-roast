# The Long Roast: Lawmakers and the File They Cannot Convert

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/yudhisutawan77/makefun-long-roast/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/yudhisutawan77/makefun-long-roast/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

One satirical sentence, at most 320 characters, roasting the lawmakers
who would regulate AI, crypto or the internet but cannot convert a file
to PDF — entered in [The Long Roast: Lawmakers and the File They Cannot
Convert](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
on [make.fun](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7).

## The entry

> The chairman who regulates AI, crypto, and the internet just asked IT
> to install 'the PDF button,' then emailed the committee a photo of his
> monitor with the subject line 'bill attached.'

(187 characters, one sentence.)

The setup grants the chairman his authority — he regulates AI, crypto,
and the internet — and the turn undercuts it twice: first he asks IT to
install "the PDF button," then the bill itself reaches the committee as
a photograph of his monitor, subject line "bill attached."

## How it works

`main.py` is stdlib-only. It validates the sentence (non-blank, exactly
one sentence, at most 320 characters) and writes it to
`/output/entry.txt`, printing it to stdout as well.

```sh
python3 main.py
```

Set `ENTRY_OUT` (or `ENTRY_OUT_DIR`) to write the entry somewhere else
when testing locally.
