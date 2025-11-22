# decrypt_calculated.py
from Crypto.Util.number import long_to_bytes
from sympy import mod_inverse

# RSA public parameters
n = 130033
e = 65537

# FACTORED p and q (computed manually or via brute-force)
p = 17
q = 7649

# Step 1: Compute phi(n)
phi = (p - 1) * (q - 1)

# Step 2: Compute private exponent d = e^{-1} mod phi(n)
d = mod_inverse(e, phi)
print("[+] Computed d =", d)

# Step 3: Load ciphertext
with open("ciphertext.txt", "r") as f:
    c = int(f.read().strip())

# Step 4: Decrypt m = c^d mod n
m = pow(c, d, n)

# Convert to bytes (auto size)
pt = long_to_bytes(m)

print("[+] Decrypted bytes:", pt)
print("[+] Hex:", pt.hex())

try:
    print("[+] Decrypted message:", pt.decode())
except UnicodeDecodeError:
    print("[-] Cannot decode as UTF-8. Maybe wrong keys or non-text content.")
