MORSE_CODE_DICT = {
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
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def encrypt(text):
    result = ""
    for item in text.upper():
        result += MORSE_CODE_DICT.get(item, "") + " "
    return result


def decrypt(text):
    morse_to_letter = {v: k for k, v in MORSE_CODE_DICT.items()}
    result = ""
    for item in text.split(" "):
        result += morse_to_letter.get(item, " ")
    return result


def main():
    print(encrypt("Hello World"))
    print(decrypt(".... . .-.. .-.. ---  .-- --- .-. .-.. -.. "))


if __name__ == "__main__":
    main()
