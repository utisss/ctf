# Web: ImpostorRenderer
In this challenge, a site is provided which renders PDFs from HTML. 
The renderer has been insecurely configured to be able to read local files, 
so the `file://` URI can be used to read the flag at `/flag.txt`. 
For example, rendering the following payload reveals the flag:

`<iframe src="file:///flag.txt"></iframe>`

## Prompt
The imposters have formed a corporation and now they're demoing a new 
software product online. Can you help me exploit the site to read the 
imposter's secrets?

_by mattyp_

## Hint
The flag is stored at `/flag.txt`.

## Flag
`utflag{l0cal_f1l3_1nclus10n_c0n51d3r3d_harmfu1}`
