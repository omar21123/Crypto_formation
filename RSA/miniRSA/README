# Mini RSA Challenge – README

This folder demonstrates a **classic CTF vulnerability in RSA**: when the public exponent **e = 3** is used *without padding*, and the message is small enough, RSA becomes completely broken.

This project includes:

* `encrypt.py` → encrypts a message with a weak RSA configuration
* `decrypt.py` → recovers the plaintext using the cube root attack

---

## 🔐 1. Understanding the Mini RSA Vulnerability

RSA encryption is:

```
c = m^e mod N
```

When:

* exponent **e = 3** is very small
* the message **m is small** (and *m³ < N*)

Then:

```
c = m^3    (because m^3 < N → no modulo reduction)
```

So the ciphertext is just a perfect cube.

➡️ Anyone can recover the message by simply computing the **integer cube root** of the ciphertext.

This is known as the **low-exponent RSA attack / Small exponent attack**.

---

## ⚙️ 2. encrypt.py – Weak RSA Encryption

The encryption script uses a massive modulus **N**, but keeps **e = 3**, making it vulnerable.

### Steps done by encrypt.py

1. Define RSA public key:

```
N = <large number>
e = 3
```

2. Convert the plaintext into an integer:

```
m = bytes_to_long(message)
```

3. Encrypt:

```
c = m^e mod N
```

Because **m is small**, the result is:

```
c = m^3  (no mod reduction)
```

### Example

Input message:

```
message = b"SECOPS{mini_rsa_test}"
```

Output ciphertext:

```
Ciphertext: <large integer>
```

---

## 🔓 3. decrypt.py – Cube Root Attack (No Private Key Needed)

This is the main point of the challenge:

You **DO NOT** need p or q.
You **DO NOT** need φ(n).
You **DO NOT** need d.

Just compute:

```
m = ³√c
```

### Steps in decrypt.py

1. Load ciphertext:

```
c = gmpy2.mpz(cipher)
```

2. Compute the integer cube root:

```
root, exact = gmpy2.iroot(c, 3)
```

3. Convert back to bytes:

```
hex_msg → unhexlify → plaintext
```

Output:

```
Recovered plaintext: b'SECOPS{mini_rsa_test}'
```

---

## 📚 4. Why This Attack Works

For RSA to be secure, the message must be padded with:

* PKCS#1 v1.5
* OAEP
* or another secure padding scheme

Without padding + e = 3 → the encryption becomes reversible.

This is a classic CTF challenge because:

* Large N tricks beginners
* But e = 3 with a small message instantly destroys security

---

## 🧠 5. Summary

This challenge teaches:

### ✔ How RSA encryption works internally

### ✔ Why small exponent e=3 is dangerous

### ✔ How to attack RSA using cube root

### ✔ How to exploit unpadded RSA systems in CTFs

---

## 📁 Files Overview

```
miniRSA/
│ encrypt.py     # Performs vulnerable RSA encryption (m^3)
│ decrypt.py     # Recovers message with integer cube root
```
