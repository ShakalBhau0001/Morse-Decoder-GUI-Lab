import customtkinter as ctk

MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    " ": "/",
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text):
    text = text.upper()
    return " ".join(MORSE_CODE[c] for c in text if c in MORSE_CODE)


def morse_to_text(morse):
    decoded = ""
    for code in morse.split(" "):
        decoded += REVERSE_MORSE.get(code, "")
    return decoded


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Morse Decoder CLI → GUI Lab")
app.geometry("700x500")
title = ctk.CTkLabel(
    app, text="🔤 Morse Decoder GUI Lab", font=("Consolas", 22, "bold")
)
title.pack(pady=10)
input_box = ctk.CTkTextbox(app, height=120, font=("Consolas", 14))
input_box.pack(padx=20, pady=10, fill="x")
output_box = ctk.CTkTextbox(app, height=120, font=("Consolas", 14))
output_box.pack(padx=20, pady=10, fill="x")


def encode_action():
    text = input_box.get("1.0", "end").strip()
    output_box.delete("1.0", "end")
    output_box.insert("end", text_to_morse(text))


def decode_action():
    morse = input_box.get("1.0", "end").strip()
    output_box.delete("1.0", "end")
    output_box.insert("end", morse_to_text(morse))


button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=15)
encode_btn = ctk.CTkButton(button_frame, text="Text → Morse", command=encode_action)
encode_btn.grid(row=0, column=0, padx=15)
decode_btn = ctk.CTkButton(button_frame, text="Morse → Text", command=decode_action)
decode_btn.grid(row=0, column=1, padx=15)
footer = ctk.CTkLabel(
    app, text="CLI Logic • GUI Layer • Learning Lab", font=("Consolas", 12)
)
footer.pack(pady=10)

app.mainloop()
