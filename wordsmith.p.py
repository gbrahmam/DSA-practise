def word_smith(forbidden_alphabets):
    # You can start from here
    
    def chopper(inputstring):
        
        for i in inputstring:
            if i not in forbidden_alphabets:
                continue
            else:
                i = ' '
		print(inputstring)
	    # return inputstring
    
    return chopper
    
### Do not change anything below this line.
if __name__ == "__main__":
    alphabets = [i for i in input().split(' ')]
    inputstring = input()
    chopper = word_smith(alphabets)
    print(chopper(inputstring))