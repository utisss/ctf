#!/usr/bin/env python3

import yaml
import re
import secret

naughty_list = """
naughty_list:
- Donald Trump
- Joe Biden
- DB Cooper
- Jonathan Browne
"""

print("Who do you want to add to the naughty list?")
new_name = input()
if re.match("^[A-Za-z ]+$", new_name):
    naughty_list += "\n- " + new_name
else:
    print("Invalid name")
print("Here is the current naughty list:")

try:
    for name in yaml.load(naughty_list, yaml.Loader)["naughty_list"]:
        print(name + " is naughty")
except:
    print("The naughty list got corrupted!")
    print(secret.flag)
