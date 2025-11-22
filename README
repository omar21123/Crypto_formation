# 🛡️ Crypto Formation – Complete Guide (CTF Oriented)

Bienvenue dans la **formation complète en cryptographie appliquée CTF**.
Ce README global couvre toutes les parties du dossier `Crypto_formation/` : **hashing, cracking, CyberChef, RSA, brute-force, mini challenges**, et méthodologie générale.

---

## 📌 Table of Contents

1. 🔐 Introduction
2. 🧂 Hashing & Password Cracking

   * Types de hash
   * Extraction d'un hash
   * Hashcat usage
   * Cracking ZIP / RAR
   * JohnTheRipper
3. 🍳 CyberChef – Crypto forensics
4. 🔢 RSA Fundamentals

   * Encryption / Decryption
   * Key generation
   * MiniRSA Vulnerabilities
   * RSA attacks (CTF)
5. 🚀 RSA Brute-force & Factoring
6. 🧩 Mini Challenges (CTF Format)
7. 📁 Structure of the repository
8. 📚 Useful commands & Tools summary

---

# 🔐 1. Introduction

Cette formation couvre les bases nécessaires pour résoudre des challenges cryptographiques **orientés CTF**.
Objectifs :

* Comprendre les types de cryptographie utilisés en challenge
* Savoir extraire, analyser et casser des hashs
* Utiliser CyberChef efficacement
* Manipuler RSA : encrypt, decrypt, attaques classiques
* Automatiser avec Python
* Construire une méthodologie solide

Format CTF utilisé : `SECOPS{...}`

---

# 🧂 2. Hashing & Password Cracking

## 🔸 2.1 Types de hash

Les plus communs :

* MD5
* SHA1 / SHA256
* Bcrypt
* NTLM
* des hashes de ZIP/RAR

Pour identifier un hash :

```bash
hashid fichier.txt
```

ou avec `hashcat --example-hashes`.

---

## 🔸 2.2 Extraire un hash (ZIP, fichiers…)

ZIP classique :

```bash
zip2john secret.zip > hash.txt
```

RAR :

```bash
rar2john file.rar > hash.txt
```

Ensuite casser le hash avec Hashcat.

---

## 🔸 2.3 Hashcat – Commands essentielles

### Crack MD5

```bash
hashcat -m 0 hash.txt /usr/share/wordlists/rockyou.txt
```

### SHA256

```bash
hashcat -m 1400 hash.txt rockyou.txt
```

### ZIP

```bash
hashcat -m 13600 zip_hash.txt rockyou.txt
```

### RAR

```bash
hashcat -m 13000 rar_hash.txt rockyou.txt
```

---

## 🔸 2.4 JohnTheRipper – Commands essentielles

ZIP/RAR/Custom :

```bash
john hash.txt --wordlist=rockyou.txt
```

Voir les résultats :

```bash
john --show hash.txt
```

---

# 🍳 3. CyberChef – Crypto Forensics

Outil indispensable pour :

* XOR
* ROT
* Base64
* Hex ↔ ASCII
* AES / DES
* Décoder des dumps bizarres

Exemple XOR :

```
Input → XOR → Key: 0x42 → Output
```

Exemple Base64 :

```
From Base64 → Output: SECOPS{flag}
```

---

# 🔢 4. RSA Fundamentals

## 🔸 4.1 Encrypt formula

```
c = m^e mod n
```

## 🔸 4.2 Decrypt formula

```
m = c^d mod n
```

Où :

* n = p × q
* φ = (p-1)(q-1)
* d ≡ e⁻¹ mod φ

---

## 🔸 4.3 Code RSA simple (encrypt/decrypt)

```python
from Crypto.Util.number import *
p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537
phi = (p-1)*(q-1)
d = inverse(e, phi)

msg = b"SECOPS{rsa_test}"
m = bytes_to_long(msg)
c = pow(m, e, n)
pt = long_to_bytes(pow(c, d, n))
print(pt)
```

---

# 🧨 4.4 MiniRSA – Vulnérabilités utilisées en CTF

Vulns classiques :

* **low exponent attack (e=3)** sans padding
* **small n** → bruteforce
* **faulty nonce** (rare)
* **CRT fault** (avancé)

Exemple low exponent attack :

```python
root, exact = gmpy2.iroot(c, 3)
print(bytes.fromhex(format(root, 'x')))
```

---

# 🚀 5. RSA Brute-force & Factoring

Pour un petit **n**, on factorise p,q :

```python
for i in range(2, isqrt(n)):
    if n % i == 0:
        print(i, n//i)
```

Solution multi-thread (existe dans ton dossier `RSA_BruteForce/`).

---

# 🧩 6. Mini Challenges (Format CTF)

### Challenge de hash :

```
MD5 → crack → SECOPS{password}
```

### Challenge RSA e=3 :

```
Root cube → décoder → SECOPS{rsa_cracked}
```

### XOR CyberChef :

```
XOR bruteforce → révéler flag
```

---

# 📁 7. Repository Structure

```
Crypto_formation/
├── hash/          → extraction, hashcat, zip2john, challenges
├── RSA/           → rsa brute force + miniRSA
└── README.md      → ce document
```

---

# 📚 8. Useful Commands Summary

| Tool       | Command                                |
| ---------- | -------------------------------------- |
| zip2john   | `zip2john file.zip > hash.txt`         |
| rar2john   | `rar2john file.rar > hash.txt`         |
| hashid     | `hashid file`                          |
| hashcat    | `hashcat -m <ID> hash.txt rockyou.txt` |
| john       | `john hash.txt --wordlist=rockyou.txt` |
| python RSA | `pow(c, d, n)`                         |

---

# ✔️ Conclusion

Cette formation te donne la base complète pour résoudre 90% des challenges crypto CTF.
