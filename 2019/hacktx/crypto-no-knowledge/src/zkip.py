def verify1(g, p, C):
    print("Send me r: ")
    r = input()
    if r.isnumeric():
        r = int(r)
        return C == pow(g, r, p)
    return false


def verify2(g, p, y, C):
    print("Send me (x + r) mod (p - 1): ")
    xr = input()
    if xr.isnumeric():
        xr = int(xr)
        return (C*y % p) == pow(g, xr, p) 
    return false
    

def proof_round(g, p, y, n):
    print("Compute a random number r and send me g^r mod p: ")
    C = input()
    if C.isnumeric():
        C = int(C)
        if n % 2 == 0:
            return verify1(g, p, C)
        else:
            return verify2(g, p, y, C)

def main():

    # WILL SMITH's public parameters
    g = 2
    p = 9375119790450996218800455883451345336695855790791241020058042501987900920600528738223355476522262581439097496402411226460716471247425673326484948646632061
    y = 5954245469284513610947819945924138072213664706770638382722170958711863430250348082109154748988457221560891498741505152926581333481648986146668353438353092

    print("Are you actually WILL SMITH?? Prove it to me by playing my stupid game!")
    print("Don't worry Mr. Smith, if you play my game I will have ZERO KNOWLEDGE of your secret password x :^)")

    flag = True
    
    for i in range(1, 101):
        print("ROUND " + str(i))
        if proof_round(g, p, y, i):
            print("OK NEXT ROUND")
        else:
            print("You are not WILL SMITH!")
            flag = False
            break
    
    if flag:
        with open('FLAG.txt', 'r') as f:
            print(f.readlines()[0].strip())

main()
