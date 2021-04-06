file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("There are {} of {} files".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())