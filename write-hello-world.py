# Will iterate through the text and individually print each letter on the same line.
def write_complicated(text='Hello World!'):
    for letter in text:
    	print(letter, end = '')
    print('')

if __name__ == "__main__":
    write_complicated()
