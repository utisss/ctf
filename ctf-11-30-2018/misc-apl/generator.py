
flag = "utflag{mushrooms_beat_them_apples_handedly}"

result = "res←bad["
for char in flag:
    result += "("
    result += str(int(ord(char) / 10) - 8)
    result += " "
    result += str(ord(char)  % 10 + 1)
    result += ")"
result += "]"
print(result)

