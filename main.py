import string

print("Caesar's cypher")
dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
msg = input("Type your message:\n").lower()
shift = input("Type the shift number:\n")

alpha_len = len(string.ascii_lowercase)

def caesar(msg, shift):
    shift = int(shift)
    if shift > 26:
        shift = shift%26
    new  = ''
    if dir == "encode":
        for n in msg:
            if n == " ":
                new += " "
            else:
                shifted = string.ascii_lowercase.index(n)+shift
                if shifted < alpha_len:
                    new += string.ascii_lowercase[shifted]
                else:
                    new += string.ascii_lowercase[shifted-alpha_len]
        print(f"The encoded message is {new}")
    elif dir == "decode":
        for n in msg:
            if n == ' ':
                new += " "
            else:
                shifted = string.ascii_lowercase.index(n)-shift
                if shifted >= 0:
                    new += string.ascii_lowercase[shifted]
                else:
                    new += string.ascii_lowercase[alpha_len+shifted]
        print(f"The decoded message is {new}")

caesar(msg, shift)