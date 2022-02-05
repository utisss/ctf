# \[Forensics\] - LSBeans

#### Points = 100

## Prompt

Wow! Legumes sure are colorful! I wonder how computers understand and display colors.

By Aly Abdulatif (Prince_Ali#9152)

#### Hints
\[None\]

## Provided Files

[legumes.png](./legumes.png)

## Write Up

- when doing steganography problems look closely for hints in the prompt, but here is a good general [checklist](https://stegonline.georgeom.net/checklist)
- In this specific problem, the flag was hidden using [LSB](https://mikeward.net/steganography/steganography-lsb/) encoding.
- [CyberChef](https://gchq.github.io/CyberChef/#recipe=Extract_LSB('R','G','B','','Row',0)) is very useful for extracting messages hidden using LSB.

## Flag

utflag{colors_hide_as_much_as_they_reveal}
