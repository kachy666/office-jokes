# Make the AI Judge Laugh: Office Jokes

Entry for the make.fun competition
**u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a**
("Make the AI Judge Laugh: Office Jokes", $5 prize pool, free entry).

## The joke

> I replied-all 'please stop replying-all' and got promoted to head of communications.

One line about office life (84 characters). The setup is the most universal
office truth there is — the reply-all storm, where every "please stop
replying-all" only feeds the thread — and the turn lands somewhere the reader
does not see coming: instead of a reprimand, the complainer gets promoted
for it. The laugh comes with a wince, because everyone who has ever worked
in an office has lived that thread.

## How it works

`main.py` holds the joke as a literal, validates it (1–199 characters, not
only white space, failing loudly otherwise), and writes it to
`/output/entry.txt`, which is what the competition's sealed gate scores and
the judge reads.

Run it with:

```sh
python3 main.py
```

## Files

- `main.py` — the entry program (shebang, validation, writes `/output/entry.txt`)
- `LICENSE` — MIT license
- `README.md` — this file
