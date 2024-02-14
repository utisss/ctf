# YAML sucks

YAML interprets bare text as strings. So this is a list of strings:

```yaml
- Donald Trump
- Joe Biden
- DB Cooper
- Jonathan Browne
```

Unless the bare text happens to be a special keyword. So is a list of not-strings:

```yaml
- yes
- no
- true
- false
- null
```

In Python, trying to concatenate a string with a not-string will error out, so typing any of these will dump the flag.
