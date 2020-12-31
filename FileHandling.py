f1 = open("tp.txt", "r")

# Read contents Line by line
print(f1.readline())

f2 = open("abc.txt", "a")

# Copy all contents from file1 to file2
for data in f1:
    f2.write(data)