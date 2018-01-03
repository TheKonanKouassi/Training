#
# Save a files
#

text = 'Sample Text to save\nNew line'

saveFile = open('exampleFile.txt', 'w')

saveFile.write(text)

saveFile.close()

#
# Appending files
#

appendME = '\n New bit of information'

appendFile = open('exampleFile.txt', mode='a')

appendFile.write(appendME)

appendFile.close()
