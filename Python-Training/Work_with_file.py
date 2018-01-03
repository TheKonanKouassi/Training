#
# Save a file
#

text = 'Sample Text to save\nNew line'

saveFile = open('exampleFile.txt', 'w')

saveFile.write(text)

saveFile.close()

#
# Appending file
#

appendME = '\n New bit of information'

appendFile = open('exampleFile.txt', mode='a')

appendFile.write(appendME)

appendFile.close()


#
# Read from a file
#

readMe = open('exampleFIle.txt', 'r')

print(readMe.readlines())

