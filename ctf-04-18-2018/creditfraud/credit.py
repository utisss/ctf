
def luhn(n):        
    sum = 0
    alt = 0
    i = len(n) - 1
    num = 0
    while i >= 0:
        num = int( n[ i ] )
        if alt:
            num = num * 2
            if num > 9:
                num = ( num % 10 ) + 1  
        sum = sum + num 
        alt = not alt 
        i -= 1
    return sum%10 == 0

while True:
    number = str(input())
    if not luhn(number):
        print number

