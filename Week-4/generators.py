# using generator in file handling

def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

g = read_file("file_handling/sample_files/sample_file.txt")
for line in g:
    if "error" in line:
        print(line)

# for line in g:
#     print(line)       wont work as generator is exhausted





# a generator allows pausing/resuming

def genr():
    for i in range(10):
        yield i

g1 = genr()

for i in g1:
    if i > 5:
        break
    print(i)

print('break occurs at: ', i)    # i = 6 is fetched by next() but not printed

print('remaining elements:')
for i in g1:
    print(i)


# yield pauses the function and saves its state, so it can resume from the same point when called again.