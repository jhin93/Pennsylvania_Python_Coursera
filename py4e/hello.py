fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    _, _, floatExtracted = line.partition(":")
    convertedFloat = float(floatExtracted)
    total += convertedFloat
    count +=1

print("Average spam confidence:", total / count)