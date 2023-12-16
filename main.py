text = str(input())
text = text.upper()
text_to_array = []
morza_ans = ''
morza = {"A": ".-", "B": "-..", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "...", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--","O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W":".--", "X": "-..-", "Y": "-.--", "Z": "--.."}
for c in text:
    text_to_array.append(c)
for letter in text_to_array:
    if morza.__contains__(letter):
        morza_ans += " " + morza[letter]

print(morza_ans)

morza_to_array = morza_ans.split(" ")



