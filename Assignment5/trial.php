from sys import argv

script, filename = argv

txt = open(C:\Users\Sai Monika Tadaka\Documents\Data Visualization\Assignment5\avg.txt)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()