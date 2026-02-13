words = ["tea", "bat", "tab", "tan", "eat", "ate"]

anagrams = {}

for word in words:
    key = ''.join(sorted(word))   # sort letters
    if key in anagrams:
        anagrams[key].append(word)
    else:
        anagrams[key] = [word]

# Print result
for group in anagrams.values():
    print(group)
