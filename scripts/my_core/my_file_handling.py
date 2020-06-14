import sys
# print(sys.getdefaultencoding()) # to check default encoding of the system

# open function return a file-like object
f = open("../data_files/out.txt", mode='wt', encoding='utf-8')  # modes r=read, w=write, a=append. # selector t=text, b=binary
#print(f, type(f))  # <_io.TextIOWrapper name='../data_files/out.txt' mode='wt' encoding='utf-8'> <class '_io.TextIOWrapper'>
code_points1 = f.write("Recent tragedies in the US have shone a spotlight on the racism and injustice "
        "faced by Black people around the world, including in the UK.\n")
# code_points are the character written to the file
# A code point is the atomic unit of information. Text is a sequence of code points.
# Each code point is a number which is given meaning by the Unicode standard.
# A code unit is the unit of storage of a part of an encoded code point. In UTF-8 this means 8-bits, in UTF-16 this
# means 16-bits. A single code unit may represent a full code point, or part of a code point. For example,
# the snowman glyph (☃) is a single code point but 3 UTF-8 code units, and 1 UTF-16 code unit.
print(code_points1)  # Returns 139 code points
code_points2 = f.write("Formula 1 cancels races in Azerbaijan, Singapore, Japan.\n")
print(code_points2)  # Returns 57 code points
# its caller responsibility to provide new line char.
f.close()
# Windows will have one more extra byte than the linux system due to universal newline feature.

g = open("../data_files/out.txt", mode='rt', encoding='utf-8')
print(f"#{g.read(139)}#")  # number of charters to read, not the byte, Result has new line char at the end
print(f"#{g.read()}#")  # Read remaining data from the pointer, Result has new line char at the end
print(f"#{g.read()}#")  # result in empty string
g.seek(0)  # moving the pointer to beginning of the file, return value is new file pointer position
# seek method can only accept value of 0 or the return value of tell method how seek(10) was working. I wonder why?

print(f'#{g.readline()}#')  # Read data till the newline char
print(f'#{g.readline()}#')
print(f'#{g.readline()}#')  # Again result in empty string
g.seek(0)

lines = g.readlines()  # Results in list of all the line, Including the newline char
print(lines)

# File-like object (g) supports iteration
g.seek(0)  # before reading the data using readlines, make file pointer is at the beginning of the file
for line in g.readlines():
    print(f';;{line};;')

g.seek(0)
for line in g.readlines():
    sys.stdout.write(line)  # this will print on the console with the extra line
g.close()

# With-blocks are used in python for managing resources
# it can be used with any objects which support context managers protocols
