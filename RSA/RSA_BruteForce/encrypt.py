# encrypt.py
from Crypto.Util.number import bytes_to_long

# Weak RSA key (example)
p = 17
q = 7649
n = 130033
e = 65537

# Small message required: m < n
message = b"HI"
m = bytes_to_long(message)

c = pow(m, e, n)

with open("ciphertext.txt", "w") as f:
    f.write(str(c))

print("[+] Ciphertext generated:")
print(c)
