text = "apple banana apple orange banana apple"
words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word frequency:", freq)
