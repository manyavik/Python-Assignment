import math

# 1: Prime Number Generator (find_primes)
def find_primes(x, y):
    primes = []
    for num in range(min(x, y), max(x, y) + 1):
        if is_prime(num):
            primes.append(num)
    return primes
    
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1): #the factor of n would be less than sqrt(n)
        if num % i == 0:
            return False
    return True

print(find_primes(10, 30))

# 2: Number to Words Converter

def toWord(x):
    ones = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if (x == 0):
        word = "zero"
    if (x > 0 and x < 10):
        word = ones[x]
    if (x > 9 and x < 20):
        word = teens[x - 10]
    if (x>=20 and x<=99):
        onesVal = int(x % 10)
        tensVal = int((x - onesVal)/10)
        word = tens[tensVal] + "-" + ones[onesVal]
    if (x>=100 and x<=999):
        onesVal = int(x%10)
        tensVal = int(((x-onesVal)/10)%10)
        hundredsVal = int(x / 100)
        word = ones[hundredsVal] + " hundred " + tens[tensVal] + "-" + ones[onesVal]
    return word

print(toWord(999))

