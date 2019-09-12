# Regenerate problem
```
zip --encrypt secret.zip secret.jpg
Enter password: pickle
```

# Solution

Replace `john/run/` with your JtR install path.

```
john/run/zip2john secret.zip > zip.hashes && john/run/john zip.hashes
```

Flag is `utflag{pickle_rick}`.
