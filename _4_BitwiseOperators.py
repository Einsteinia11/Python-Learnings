#* Bitwise Operators
# Bitwise operators are operators that perform operations directly on the binary representation (bits) of integers.

#! Bitwise and &
a = 5
b = 3
print(a&b) #1
# 0101
# 0011
# ----
# 0001

#! Bitwise or |
# 0101
# 0011
# ----
# 0111
print(a|b) #7

#! Bitwise XOR ^
# 0101
# 0011
# ----
# 0110
print(a^b) #6

#! Bitwise Not ~ 
#Inverts all bits (1 → 0, 0 → 1).
print(~5) #-6

#! Left Shift <<
# Equivalent to multiplying by 2^n
print(5<<1) #10
# 0101 → 1010

#! Right Shift (>>)
# Equivalent to dividing by 2^n
print(5>>1) #2
# 0101 → 0010


a = [1, 2, 3, 2, 3]
b = [5, 3, 2, 2]
u = []
for i in a:
    for j in b:
        if i^j == 0:
            u.append(i)
        else:
            continue
print(u)