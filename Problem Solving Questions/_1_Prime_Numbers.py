def is_prime(num):
    if num>10:
        for i in range(2, 9):
            if num%i == 0:
                return False
        return True
    elif num==2:
        return True
    elif num == 1:
        return False
    elif num == 3:
        return True
    else:
        l = num-1
        for i in range(2, l):
            if num%i == 0:
                return False
        else:
            return True
print(is_prime(25))