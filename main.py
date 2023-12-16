text = str(input())
text = text.upper()
chars = []
ans = ''
morza = {"A": ".-", "B": "-..", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "...", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--","O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W":".--", "X": "-..-", "Y": "-.--", "Z": "--.."}
for c in text:
    chars.append(c)
for letter in chars:
    if morza.__contains__(letter):
        ans += morza[letter]

print(ans)
