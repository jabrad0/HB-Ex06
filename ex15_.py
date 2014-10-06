from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read(), "\n"

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)



txt.close()
txt_again.close()