try:

    file = open('../data/titanic.csv')

except FileNotFoundError:

    print('Sorry the file does not exist')

except Exception as e:

    print('Sorry Something went wrong')

    print(e)

else:

    print(file.read())

    file.close()

finally:

    print("Executing Finally....")
