# 🔐 Encryption & Decryption System — Python CLI Tool

> A command-line encryption and decryption tool supporting multiple BaseX encoding schemes: **Base16**, **Base32**, **Base64**, and **Base85**.  
> Developed in **Python** for learning and demonstration purposes.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![CLI Tool](https://img.shields.io/badge/CLI-Tool-orange?logo=gnometerminal&logoColor=white)](https://en.wikipedia.org/wiki/Command-line_interface)
[![Base Encoding](https://img.shields.io/badge/Base-Encoding-yellow?logo=lock&logoColor=black)](https://en.wikipedia.org/wiki/Base64)
[![Base16](https://img.shields.io/badge/Base16-Hexadecimal-red?logo=lock&logoColor=white)](https://en.wikipedia.org/wiki/Hexadecimal)
[![Base32](https://img.shields.io/badge/Base32-Encoding-yellow?logo=lock&logoColor=black)](https://en.wikipedia.org/wiki/Base32)
[![Base85](https://img.shields.io/badge/Base85-Encoding-brightgreen?logo=lock&logoColor=white)](https://en.wikipedia.org/wiki/Ascii85)
[![Repetition](https://img.shields.io/badge/Repetition-Loop-blueviolet?logo=repeat&logoColor=white)](https://en.wikipedia.org/wiki/Control_flow#Loops)

---

## 📖 Introduction
The **Encryption & Decryption System** is a lightweight Python-based program that allows you to securely **encode** and **decode** messages using different BaseX encoding formats.  
It supports:
- **Base85** (highest density text encoding)
- **Base64** (common web encoding)
- **Base32**
- **Base16** (hexadecimal representation)

This is an **interactive terminal program**, perfect for practicing encoding techniques and understanding BaseX operations.

---

## ✨ Features
### 🔒 Encryption
- Choose between **Base85**, **Base64**, **Base32**, or **Base16**
- Input any UTF-8 text
- Get an encoded string instantly

### 🔓 Decryption
- Decode Base85, Base64, Base32, or Base16 strings back to plain text
- Handles invalid inputs with error messages
- ASCII input validation for correct decoding

---

## 📂 Project Structure
```bash
Encryption_Decryption-main/
├── README.md         # Project documentation
├── encode.py         # Encryption script (Base85, Base64, Base32, Base16)
└── decode.py         # Decryption script (Base85, Base64, Base32, Base16)
```

---

## 🛠 Installation Guide
1. Install Python:
   
   Ensure Python 3.8+ is installed:
   ```bash
   https://www.python.org/downloads/

2. Download or Clone the Project
   ```bash
   git clone https://github.com/LowZhiHorng/Encryption_Decryption.git
   cd Encryption_Decryption-main

3. Run the Program
   - For encryption:
     ```bash
     python encode.py
     ```

   - For decryption:
     ```bash
     python decode.py
     ```

---

## 🚀 Usage
**🔒 Encrypting a Message**
```bash
$ python encode.py

Encryption System

1. Base 85 Encryption
2. Base 64 Encryption
3. Base 32 Encryption
4. Base 16 Encryption

What's your choice? (1/2/3/4): 2
Encryption message: Hello World
Encrypted message: SGVsbG8gV29ybGQ=
```

**🔓 Decrypting a Message**
```bash
$ python decode.py

Decryption System

1. Base 85 Decryption
2. Base 64 Decryption
3. Base 32 Decryption
4. Base 16 Decryption

What's your choice? (1/2/3/4): 2
Decryption message: SGVsbG8gV29ybGQ=
Decrypted message: Hello World
```

---

## 📜 License
**This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)**

---

## 👤 Author
**Low Zhi Horng**

**📂 GitHub: [![GitHub](https://img.shields.io/badge/GitHub-LowZhiHorng-black?logo=github)](https://github.com/LowZhiHorng)**
