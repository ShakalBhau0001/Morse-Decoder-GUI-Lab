# 🔤 Morse-Decoder-GUI-Lab 🧠

A Python-based **Morse Code GUI Tool** built using customtkinter that allows users to **convert text into International Morse Code** and **decode Morse code back into readable text** through an intuitive graphical interface

This project is designed as a **learning lab** to improve:
- Encoding & decoding logic
- Pattern recognition
- Understanding symbol-based communication systems
- GUI integration over core logic

It is especially useful for **puzzle solving**, **CTF-style thinking**, and **foundational cybersecurity logic building**.

---

#### 🧱 Project Structure

```bash
Morse-Decoder-GUI-Lab/
│
├── morse_decoder.py        # Main GUI application
└── README.md               # Project documentation
```

---

#### ✨ Features

## 🔐 Text → Morse Conversion
- Converts **letters**, **numbers**, and **punctuation** into **International Morse Code**
- Uses standard dot (`.`) and dash (`-`) notation
- Represents word gaps using `/`

## 🔓 Morse → Text Decoding
- Decodes space-separated Morse code
- Converts / back into spaces
- Ignores unsupported or invalid sequences safely

## 🧪 Learning-Oriented Design
- Clean and minimal dark-themed interface
- Same logic as CLI, wrapped with GUI
- Clear separation of logic layer and UI layer
- Ideal base for future extensions

---

#### 🛠 Technologies Used

| Technology             | Role                      |
| ---------------------- | ------------------------- |
| **Python 3**           | Core programming language |
| **customtkinter**      | Modern GUI framework      |
| **Dictionary Mapping** | Morse ↔ Text conversion   |
| **GUI (Desktop App)**  | User interaction          |

---

#### 📌 Requirements

```bash
Python 3.7+
pip install customtkinter
```

Only **customtkinter** is required externally.
All other modules are standard Python libraries.

---

#### ▶️ How to Run

## 1️⃣ Clone the repository

```bash
git clone https://github.com/ShakalBhau0001/Morse-Decoder-GUI-Lab.git
```

## 2️⃣ Enter the project directory

```bash
cd Morse-Decoder-GUI-Lab
```

## 3️⃣ Run the CLI tool

```bash
python morse_decoder.py
```

## ▶️ Usage

#### 🔐 Text → Morse

1. Enter normal text in the input box
2. Click **Text → Morse**
3. Morse code output appears in the output box

## 🔓 Morse → Text 

1. Enter space-separated Morse code (`/` for space)
2. Click **Morse → Text**
3. Decoded text appears instantly

---

#### ⚙️ How It Works

## 1️⃣ Morse Mapping
- A dictionary maps characters to Morse symbols:
  ```python
  "A": ".-", "B": "-...", "C": "-.-."
  ```

## 2️⃣ Encoding
- Input text is converted to uppercase
- Each character is replaced by its Morse equivalent
- Output is space-separated Morse code

## 3️⃣ Decoding
- Morse input is split by spaces
- Reverse dictionary lookup converts Morse back to text
- `/` is translated back into a space

---

#### ⚠️ Limitations
- Morse input **must be space-separated**
- Continuous Morse without spacing is **ambiguous**
- This tool does **not brute-force spacing**
- Not intended for secure communication

---

#### 🌟 Future Enhancements
- Auto-decoding Morse without spaces
- Display multiple possible decoding outputs
- File-based input/output
- Morse signal visualization
- Integration with steganography tools

---

#### 📦 Extended / Combined Tools

This repository focuses **only on Morse code encoding & decoding** using a **GUI-based learning approach**.

For a **combined and advanced GUI implementation** involving:
- Image steganography
- Audio steganography
- Encrypted payload embedding

please refer to:

> 🔗 **[StegaVault-GUI](https://github.com/ShakalBhau0001/StegaVault-GUI)**

---

#### ⚠️ Disclaimer

This project is intended for **educational and learning purposes only**.

Morse code is **not encryption** and should not be used for secure communication.
The goal is to improve **analytical thinking**, **decoding skills**, and **tool-building fundamentals**.

---

#### 🪪 Author

> **Creator: Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---
