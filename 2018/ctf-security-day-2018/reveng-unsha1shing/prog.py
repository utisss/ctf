import hashlib

secret = str.maketrans( 
    "dlpswqvajxkomebztngruiyhf", 
    "ylketiowhcqbfgjuaszxdmrpn")


flags = [663623865031686838022233277218358089514224407515,
        1390003923901765546293758696851712101473919922909,
        261279079905281052517688504948658661945099391553,
        23997393672990737301512763737290807653636425769,
        1107973472593048685754468119784108237562626563860,
        1399293205494154857242560672177008890201745470839]

flags.append(1003279347462860391980606427621107609239748558896)

print("so whats the flag")
flag = input("input the flag: ")
method = str.translate("njt1", secret)

if len(flag) > 100:
    print("no")
    exit()
if len(flag) % 5 != 0:
    print("look closer")
    exit()
for i in range(0, len(flag), 5):
    s = flag[i:i + 5]
    temp = hashlib.new(method)
    temp.update(s.encode("utf-8"))
    value = int(temp.hexdigest(),16)
    if value != flags[i // 5]:
        print("r u even trying")
        exit()

print("you didn't even need me to confirm it, you have the flag")
