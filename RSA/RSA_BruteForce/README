# RSA Brute Force Challenge – README

This project demonstrates how RSA works in a CTF-like environment and how weak RSA parameters can be attacked. The folder contains four scripts:

* **brute_force.py** → factors a weak RSA modulus *n*
* **encrypt.py** → encrypts a message using RSA
* **decrypt.py** → decrypts the ciphertext using the recovered private key
* **ciphertext.txt** → holds the RSA ciphertext

---

## 🔐 1. Understanding the Challenge

RSA security depends on the difficulty of factoring **n = p × q**. In strong RSA, p and q are huge (1024+ bits). But here:

```
p = 17
q = 7649
n = 130033
```

These numbers are extremely small, so RSA becomes vulnerable to brute-force attacks.

The goal of the challenge is:

1. Brute-force the modulus n to recover p and q.
2. Compute the private key.
3. Decrypt the ciphertext.

---

## ⚙️ 2. brute_force.py – Factoring n

This script splits the search space into threads and tests each number to check if it divides n. Since n is small, brute-forcing is fast.

### How it works

* Compute `limit = sqrt(n)`
* Divide the range into chunks
* Run each chunk in a separate thread
* Check if `n % p == 0`
* If yes → `q = n // p`

### Output example

```
[*] Starting brute-force...
[+] Factors found!
p = 17
q = 7649
```

These factors let us compute the private key.

---

## 🧮 3. decrypt.py – Computing RSA Private Key and Decrypting

Once p and q are known, RSA private key generation becomes easy.

### Steps

1. Compute Euler's totient:

```
phi(n) = (p - 1) * (q - 1)
```

2. Compute private exponent:

```
d = e^{-1} mod phi(n)
```

3. Read ciphertext from **ciphertext.txt**
4. Decrypt:

```
m = c^d mod n
```

5. Convert integer to bytes

### Output example

```
[+] Computed d = 30941
[+] Decrypted bytes: b'HI'
```

---

## ✉️ 4. encrypt.py – Encrypting a Message

This script encrypts a small message (must satisfy `m < n`).

### Steps

1. Convert message bytes → integer using `bytes_to_long`
2. Compute ciphertext:

```
c = m^e mod n
```

3. Save ciphertext to `ciphertext.txt`

You can modify `message = b"HI"` to test different inputs.

---

## 🧠 5. What This Teaches

This project shows:

* Why RSA must use **large primes** (1024–4096 bits)
* How weak keys can be completely broken
* How RSA encryption/decryption works internally
* How to implement RSA manually for CTF training

It demonstrates the entire lifecycle:

**Brute-force → Factorization → Private Key Recovery → Decryption → Understanding RSA Weaknesses**

---

## 📁 Files Overview

```
RSA_BruteForce/
│ brute_force.py     # Factors n into p and q
│ decrypt.py         # Computes d and decrypts ciphertext
│ encrypt.py         # Generates ciphertext from message
│ ciphertext.txt     # Stores RSA ciphertext
```

---

## ✔️ Conclusion

This mini RSA project is intentionally weak and designed for educational and CTF practice. It helps you understand how real RSA works and why proper key sizes are essential for security.
