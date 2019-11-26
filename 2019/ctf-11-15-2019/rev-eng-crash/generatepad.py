import random
flag = "utflag{i_l0wk3y_dislike_3ating_turk3y_1ts_way_too_dry}"

otp = [random.randint(0,255) for c in flag]


inp = [c1 ^ ord(c2) for c1,c2 in zip(otp,flag)]


print(f"{flag=} \n {inp=} \n {otp=}")
