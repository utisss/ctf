import luhn
import random

def complete_numb(prefix, length):
    ccnumber = prefix
    while len(ccnumber) < length - 1:
        ccnumber = ccnumber + str(random.randint(0,10))

    result = luhn.append(ccnumber)
    if(len(result) != length):
        return complete_numb(prefix, length)
    return result


credits = ["4532", "3466", "6011", "5120"]
out = open("isthisfraud.txt", "wb")

for i in range(5000000):
    choice = random.randint(0,3)
    if i == 492910:
        out.write("6011535950293122\n")
    out.write(complete_numb(credits[choice], 16)+"\n")

