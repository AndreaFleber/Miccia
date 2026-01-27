import random

# Legge il testo
with open("testo.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()

# Se non ci sono più parole, esce
if len(words) <= 1:
    exit()

# Calcola il centro
center = len(words) // 2

# Sceglie una parola vicino al centro
offset = random.choice([-2, -1, 0, 1, 2])
index = max(0, min(len(words) - 1, center + offset))

# Rimuove la parola
del words[index]

# Riscrive il testo
new_text = " ".join(words)

with open("testo.txt", "w", encoding="utf-8") as f:
    f.write(new_text)
