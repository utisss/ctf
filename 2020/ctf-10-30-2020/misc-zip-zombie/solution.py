import os
from zipfile import ZipFile

ZIP_NAME = 'flag.zip'
TMP_ZIP_NAME = 'tmp_' + ZIP_NAME

done = False

while not done:
	os.rename(ZIP_NAME, TMP_ZIP_NAME)
	with ZipFile(TMP_ZIP_NAME, 'r') as zp:
		zp.namelist()
		zp.extractall()
		if len(zp.namelist()) != 1 or zp.namelist()[0] != ZIP_NAME:
			done = True
	os.remove(TMP_ZIP_NAME)
