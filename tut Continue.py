notAllowed = [2, 4, 8, 16]

print("Allowed numbers:")

for x in range(1, 21):
    if x in notAllowed:
        continue
    print(x)