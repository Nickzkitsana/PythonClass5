def Types_of_integer (*data):
    Clean_data = sorted(tuple(set(data)),reverse=False)
    for i in Clean_data:
        if i == 0:
            print("{0:3} : Number is Zero".format(i))
        elif i == 1:
            print("{0:3} : Number is One".format(i))
        elif PrimeCheck(i):
            print("{0:3} : Number is Prime Number".format(i))
        else:
            print("{0:3} : Number is Composite Number".format(i))

def EzPrimeCheck(Num):
    #if Num < 2:
    #    return False

    for n in range(2, (Num) - 1):
        if Num % n == 0:
            return False
    return True

def PrimeCheck(Num):
    if Num < 3 == 0:
        return True
    if Num % 2 == 0:
        return False
    if Num % 3 == 0:
        return False
    if Num % 5 == 0:
        return False
    for n in range(2, Num -1):
        if Num % n == 0:
            return False
    return True

def AKSPrimeCheck(a):
    if a < 2:
        return False
    elif a!=2 and a % 2 == 0:
        return False
    else:
        return all (a % i for i in range(3, int(a**0.5)+1))

if __name__ == '__main__':
    Types_of_integer(10,9,22,32,45,9,2,103,71,45)
    print()
    Types_of_integer(49,37,14,37)
