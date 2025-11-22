Parfait ! Voici un **README.md complet et prêt à copier** dans ton dépôt GitHub. Tu n’as plus qu’à créer le dossier `hash_course` et mettre ce fichier dedans.

---

```markdown
# Cours Hash et CTF

## 🔐 1. Qu’est‑ce qu’un hash ?

Un **hash** est une fonction cryptographique qui transforme un message en une empreinte :

- **Unidirectionnelle** : impossible de retrouver le message d’origine.
- **Taille fixe** : 128, 160 ou 256 bits selon l’algorithme.
- **Utilisations courantes** :
  - Stockage de mots de passe
  - Vérification d’intégrité
  - Signatures numériques
  - CTF / Pentest

### 📌 Exemples

- MD5 : `5d41402abc4b2a76b9719d911017c592`
- SHA1 : `2aae6c35c94fcfb415dbe95f408b9ce91ee846ed`
- SHA256 : `2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824`

---

## 🧩 2. Résolution d’un hash simple dans un CTF

### ✅ Étape 1 : Identifier le type de hash

Outils possibles :

- **CyberChef → “Identify Hash”**
- **HashID**
- **hash-identifier**

Exemple :

```

5d41402abc4b2a76b9719d911017c592 → MD5

````

### ✅ Étape 2 : Casser le hash

#### 🔨 CyberChef

1. Coller le hash dans l’input.
2. Essayer :
   - Brute Force
   - Dictionnaire
3. Lire le résultat dans l’output.

#### 🔨 Hashcat

| Algo   | Mode |
|--------|------|
| MD5    | 0    |
| SHA1   | 100  |
| SHA256 | 1400 |

Commande exemple :

```bash
hashcat -m 0 hash.txt rockyou.txt
````

#### 🔨 JohnTheRipper

```bash
john --wordlist=rockyou.txt hash.txt
john --show hash.txt
```

### ✅ Étape 3 : Formater le flag

```
SECOPS{mot_de_passe}
```

---

## 🧰 3. Exemple pratique

Hash donné :

```
5f4dcc3b5aa765d61d8327deb882cf99
```

1. Identifier → MD5
2. Casser avec Hashcat / John → `password`
3. Flag final :

```
SECOPS{password}
```

---

## 📦 4. Cracking ZIP protégé

### 🔍 Identifier le type de chiffrement

```bash
zipinfo -v archive.zip
```

* ZipCrypto → crackable
* AES-256 → difficile

### 🗝️ Extraire le hash

```bash
zip2john archive.zip > hash.txt
```

### 🔨 Cracker

#### Avec John

```bash
john hash.txt --wordlist=rockyou.txt
john --show hash.txt
```

#### Avec Hashcat

| Type       | Mode  |
| ---------- | ----- |
| PKZIP      | 17200 |
| WinZip AES | 23001 |

Exemple :

```bash
hashcat -m 17200 hash.txt rockyou.txt
```

### 🧪 CyberChef post-crack

* Décodage Base64 / Hex
* XOR / ROT13
* Magic → détection automatique

---

## 🎯 5. Exemple complet ZIP

1. Vérification :

```bash
zipinfo -v secret.zip
```

2. Extraction du hash :

```bash
zip2john secret.zip > hash.txt
```

3. Crack :

```bash
john hash.txt --wordlist=rockyou.txt
```

4. Extraction :

```bash
unzip secret.zip
```

5. Analyse CyberChef → flag final :

```
SECOPS{flag_du_challenge}
```

---

## 📝 6. Tableau récapitulatif

| Type de hash | Exemple abrégé | Mode Hashcat | Outils conseillés          |
| ------------ | -------------- | ------------ | -------------------------- |
| MD5          | 5d4140…        | 0            | Hashcat / John / CyberChef |
| SHA1         | 2aae6c…        | 100          | Hashcat / John             |
| SHA256       | 2cf24d…        | 1400         | Hashcat                    |
| PKZIP        | $pkzip2$…      | 17200        | John / Hashcat             |
| WinZip AES   | AES…           | 23001        | Hashcat                    |

---

## 🎁 7. Points à retenir

1. Identifier le type de hash avant de cracker.
2. Commencer par **wordlists** avant brute-force.
3. CyberChef est parfait pour tester rapidement.
4. Les flags sont toujours au format : **SECOPS{...}**
5. ZipCrypto est le chiffrement ZIP le plus courant en CTF.

```


