from zlib import compress

thing = open('file.txt', 'r')

values = []
index = 0
for line in thing:
    values.append((len(compress(line)), index))
    index += 1

values = sorted(values)
print values[0:100]
