# 🔐 Simple Encryption/Decryption Tool

This project demonstrates **encryption and decryption** using three different approaches:

1. **Manual Caesar Cipher (Basic Substitution)**
2. **Fernet (Cryptography Library)**
3. **AES (PyCryptodome Library)**

The goal is to learn **cryptography basics** and understand **symmetric encryption** in Python.
---
## 📌 Features
* Manual Caesar Cipher implementation (letters + digits, shift = 3).
* Fernet symmetric encryption (secure key management).
* AES encryption using PyCryptodome in **CBC mode** with IV.
* Step-by-step examples of how encryption & decryption works.
---
## 🛠️ Technologies
* **Language:** Python 3.x
* **Libraries:**
  * [cryptography](https://pypi.org/project/cryptography/)
  * [pycryptodome](https://pypi.org/project/pycryptodome/)
---
## ⚙️ Installation
Install dependencies before running the project:
```bash
pip install cryptography
pip install pycryptodome
```
---
## 📂 Files in this Project
1. `manual_version.py` → Implements **Caesar Cipher** manually.
2. `importing_cryptography.py` → Implements **Fernet encryption** using `cryptography`.
3. `importing_pycryptodome.py` → Implements **AES (CBC mode)** using `pycryptodome`.
---
## 🔑 How Each Version Works
### 1️⃣ Manual Version – Caesar Cipher
* Each letter/digit is shifted by **3 places** (wrap-around using modulus).
* Example:
  ```
  Input:  TaTA! 43 HI.
  Encrypted: WdWD! 76 KL.
  Decrypted: TaTA! 43 HI.
  ```
---
### 2️⃣ Cryptography – Fernet
* Uses a **secret key** generated with `Fernet.generate_key()`.
* Ensures **confidentiality, integrity, and authenticity**.
* Example:
  ```
  Key: b'v0rpu8JXUpM7zK1...'
  Input:  Hello Neha123!
  Encrypted: b'gAAAAABm...'
  Decrypted: Hello Neha123!
  ```
---
### 3️⃣ PyCryptodome – AES (CBC Mode)
* Uses **AES symmetric encryption** with a 16-byte random key.
* Requires an **IV (Initialization Vector)** to start encryption securely.
* Example:
  ```
  Key: b'\xf3\x14\xa2...'
  IV:  b'j\x90\x13...'
  Input:  Hello Neha123!
  Encrypted: b'\xaf\xce\x12...'
  Decrypted: Hello Neha123!
  ```
---
## 🚀 How to Run
Run any of the scripts:
```bash
python manual_version.py
python importing_cryptography.py
python importing_pycryptodome.py
```
## 📌 Notes

* **Manual Caesar Cipher** is only for **learning purposes**, not secure.
* **Fernet & AES** are **secure methods** used in real-world applications.
* Always **store your keys securely** if you want persistent encryption.
---
## 📘 Learning Outcomes
* Difference between **simple substitution** (Caesar) and **modern cryptography** (AES, Fernet).
* How **keys and IVs** are used for secure encryption.
* Importance of **padding** in AES (text must align with block size).
