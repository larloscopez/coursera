file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("There are {} of {} files".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, arms in cool_beasts.items():
    print("{} have {}".format(animal, arms))

# Counting Occurences of letters in text
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return print(result)

count_letters("AAAAAAAAAAAAAAAA")
count_letters("TESTIMONYAGAOINTTTT")

#dictionary vs list