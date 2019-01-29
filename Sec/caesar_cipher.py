# Solution for PicoCTF 2018 Cryptography challenge: caesar cipher 2

cipher = input("Ciphertext: ")
iterations = int(input("Number of interations: "))
flag_format = "picoCTF"

for i in range (iterations):
    plain = ""
    for char in cipher:
        rot = ord(char) + i
        plain += chr(rot)
    print(plain)
    if flag_format in plain:
        print("\n!! FOUND FLAG: " + plain)
        break
