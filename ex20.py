from sys import argv

script, input_file = argv #primes function to expect a file to work on

def print_all(f):
    print f.read() #defines function to accept the file and read everything in it

def rewind(f):
    f.seek(0) #defines fn to go back to the beginning

def print_a_line(line_count,f):
    print line_count, f.readline() #defines a fn that expects a line count and a file

current_file = open(input_file) #defines variable current_file as the file you input at the beginning

print "First let's print the whole file:\n"

print_all(current_file) #prints the whole thing

print "Now let's rewind, kind of like a tape."

rewind(current_file) #rewinds back to beginning of the file so that you can start at line 1 for the next ffn

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) #prints the first line of the file

current_line = current_line + 1
print_a_line(current_line, current_file) #feeds in line 1, adds 1, and prints line 2

current_line = current_line + 1
print_a_line(current_line, current_file) #feeds in line 2, adds 1, and prints line 3
