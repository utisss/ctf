#!/usr/bin/bash

tar cf source.tar Dockerfile app.py static templates
zstd source.tar
rm source.tar
