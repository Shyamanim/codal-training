class FileLineReader:
    def __init__(self, filename):
        self.filename = filename
        #self.file = open(self.filename)    # won't work as iterator will get exhausted

    def __iter__(self):
        self.file = open(self.filename) # opens new file on every iteration
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip()
        else:
            self.file.close()
            raise StopIteration

reader1 = FileLineReader("file_handling/sample_files/sample_file.txt")
print(type(reader1))
print("First use:")
for line in reader1:
    print(line)

print("\nSecond use:")
for line in reader1:
    if 'error' in line:
        print(line)
