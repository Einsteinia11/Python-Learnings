#This program encodes and decodes the messages
def encode(msg, shift):
    l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_msg = ""
    for i in range(0, len(msg)):
        k = -1
        for j in range(0, len(l)):
            if msg[i] == l[j]:
                k = j + shift
                if k > len(l):
                    k = (j + shift)%26
                    new_msg += l[k]
                    break
            if k == j:
                new_msg = new_msg + l[k]
                break
    print("Encoded message = ", new_msg)

def decode(msg, shift):
    l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_msg = ""
    for i in range(0, len(msg)):
        k = -len(l)
        for j in range(-1, -(len(l)+1), -1):
            print("msg[i]  = ",msg[i],"l[j] = ", l[j])
            if msg[i] == l[j]:
                k = j - shift
                print(k)
                if k < -len(l):
                    k = (j - shift)%26
                    print(k)
                    new_msg += l[k]
                    break
            if k == j:
                new_msg = new_msg + l[k]
                break
    print("Encoded message = ", new_msg)
#But Time complexity = O(26n) = O(n)
# with one loop
# def encode(msg, shift):


c = input("Enter to encode and d to decode")
msg = input("Enter message:")
shift = int(input("Enter shift:"))
if c == "e":
    encode(msg, shift)
else:
    decode(msg, shift)