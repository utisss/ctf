import random, array, struct

def packPkt(datagram, fmt):
    pkt = ''
    for d in datagram:
        pkt = pkt + struct.pack(fmt, d)

    return pkt

def unpackPkt(pkt, fmt):
    datagram = array.array('L')
    for i in xrange(0, 2):
        tup = struct.unpack_from(fmt, pkt, offset=i*4)
        datagram.append(tup[0])

    return datagram
