#!/usr/bin/env python
import sys

print("In order to gain access to the Fabulous Legitimate Access Group (FLAG), please enter your serial number.")
if len(sys.argv) < 2:
	print ("Usage: %s [serial number]"%sys.argv[0])
	exit()
  
print ("You entered serial " + sys.argv[1])

def flag_from_key(serial):
    return "utflag{" + "".join([chr(int(x) * 2 + 97) for x in serial]) + "}"

def check_serial(serial):
	if not set(serial).issubset(set(map(str,range(10)))):
		print("Your serial number must be all digits.")
		return False

	if len(serial) != 15:
		print("Wrong length")
		return False

	if int(serial[1]) + int(serial[7]) != 4:
		return False
	if int(serial[9]) + int(serial[14]) != 3:
		return False
	if int(serial[6]) - int(serial[2]) != 2:
		return False
	if int(serial[13]) + int(serial[14]) != 12:
		return False
	if int(serial[4]) + int(serial[6]) != 11:
		return False
	if int(serial[11]) - int(serial[4]) != 2:
		return False
	if int(serial[4]) - int(serial[5]) != 4:
		return False
	if int(serial[8]) + int(serial[12]) != 7:
		return False
	if int(serial[0]) * int(serial[4]) != 8:
		return False
	if int(serial[3]) * int(serial[4]) != 36:
		return False
	if int(serial[10]) - int(serial[5]) != 4:
		return False
	if int(serial[2]) * int(serial[11]) != 30:
		return False
	if int(serial[12]) * int(serial[3]) != 9:
		return False
	if int(serial[7]) / int(serial[0]) != 2:
		return False
	return True

if check_serial(sys.argv[1]):
	print ("Thank you! Your FLAG access code is {}".format(flag_from_key(sys.argv[1])))
else:
	print ("Invalid serial number. Please try again.")

