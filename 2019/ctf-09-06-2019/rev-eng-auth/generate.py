import random
flag = "utflag{I_AM_S1mpl1c10_XDXDXDXD}"
rand = [random.randint(1,200) for i in range(len(flag))]

print("rand: ", rand)
store = [(ord(ch) ^ ran) for ch,ran in zip(flag,rand)] 
print("store: ",store)

